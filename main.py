from fastapi import FastAPI, UploadFile, File, HTTPException
import duckdb
import tempfile
import shutil
import os

app = FastAPI()
duckdb.execute("INSTALL httpfs; LOAD httpfs;")  # Load extensions once at startup
MAX_FILE_SIZE = 100 * 1024 * 1024  # 100MB

@app.post("/upload-parquet")
async def upload_parquet(file: UploadFile = File(...)):
    tmp_path = None
    try:
        # Validate file type
        if not file.filename.endswith(".parquet"):
            raise HTTPException(400, "Only .parquet files are allowed")

        # Validate file size
        file.file.seek(0, os.SEEK_END)
        file_size = file.file.tell()
        if file_size > MAX_FILE_SIZE:
            raise HTTPException(413, f"File too large (> {MAX_FILE_SIZE//(1024*1024)}MB)")
        file.file.seek(0)  # Reset file pointer

        # Get file extension for temp file
        suffix = os.path.splitext(file.filename)[1]  # Added this line

        # Save uploaded file to temp path
        with tempfile.NamedTemporaryFile(delete=False, suffix=suffix) as tmp:
            shutil.copyfileobj(file.file, tmp)
            tmp_path = tmp.name

        # Query Parquet file
        query = f"SELECT * FROM read_parquet('{tmp_path}')"
        con = duckdb.connect()
        result = con.execute(query)
        
        # Process results
        columns = [desc[0] for desc in result.description]
        rows = result.fetchall()
        data = [dict(zip(columns, row)) for row in rows]
        con.close()

        return {
            "data": data,
            "columns": columns,
            "row_count": len(data)
        }

    except HTTPException as he:
        raise he  # Re-raise validation errors
    except Exception as e:
        return {"error": str(e)}
    finally:
        # Clean up temp file
        if tmp_path and os.path.exists(tmp_path):
            os.unlink(tmp_path)
