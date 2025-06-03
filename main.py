from fastapi import FastAPI, UploadFile, File
import duckdb
import tempfile
import shutil
import os

app = FastAPI()

# Install and load DuckDB's HTTP extension once at startup
duckdb.execute("INSTALL httpfs; LOAD httpfs;")

@app.post("/upload-parquet")
async def upload_parquet(file: UploadFile = File(...)):
    tmp_path = None
    try:
        # Create a temporary file with the same suffix as uploaded file
        suffix = os.path.splitext(file.filename)[1]
        with tempfile.NamedTemporaryFile(delete=False, suffix=suffix) as tmp:
            shutil.copyfileobj(file.file, tmp)
            tmp_path = tmp.name

        # Query the Parquet file
        query = f"SELECT * FROM read_parquet('{tmp_path}')"
        con = duckdb.connect()
        result = con.execute(query).fetchall()
        columns = [desc[0] for desc in con.description]
        con.close()

        return {
            "data": [dict(zip(columns, row)) for row in result],
            "columns": columns
        }
    except Exception as e:
        return {"error": str(e)}
    finally:
        if tmp_path and os.path.exists(tmp_path):
            os.unlink(tmp_path)
