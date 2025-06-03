
from fastapi import FastAPI, UploadFile, File
from pydantic import BaseModel
import duckdb
import tempfile

app = FastAPI()

# Load DuckDB's HTTP extension for remote file access
duckdb.execute("INSTALL httpfs; LOAD httpfs;")

@app.post("/upload-parquet")
async def upload_parquet(file: UploadFile = File(...)):
    try:
        # Save uploaded file temporarily
        with tempfile.NamedTemporaryFile(delete=False) as tmp:
            content = await file.read()
            tmp.write(content)
            tmp_path = tmp.name
        
        # Query the Parquet file
        query = f"SELECT * FROM read_parquet('{tmp_path}')"
        result = duckdb.query(query).fetchall()
        columns = [desc[0] for desc in duckdb.query(query).description]
        
        return {
            "data": [dict(zip(columns, row)) for row in result],
            "columns": columns
        }
    except Exception as e:
        return {"error": str(e)}
    finally:
        if tmp_path:
            os.unlink(tmp_path)
