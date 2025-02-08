from fastapi import FastAPI, UploadFile, File, HTTPException
from fastapi.responses import JSONResponse
import os
import shutil
from typing import List
from loguru import logger


app = FastAPI()

# Configure upload settings
UPLOAD_DIR = "uploads"
ALLOWED_EXTENSIONS = {".txt", ".pdf", ".doc", ".docx"}

# Create uploads directory if it doesn't exist
os.makedirs(UPLOAD_DIR, exist_ok=True)

from superteam_ai.llm.local_llm import LocalLLM

# Initialize LocalLLM
config = {
    'model_name': 'deepseek-r1:1.5b',
    'embedding_model_name': 'nomic-embed-text',
    'vector_store_path': './vector_store'
}
llm_instance = LocalLLM(config)

@app.post("/upload/")
async def upload_file(file: UploadFile = File(...)):
    try:
        # Check file extension
        file_ext = os.path.splitext(file.filename)[1].lower()
        if file_ext not in ALLOWED_EXTENSIONS:
            raise HTTPException(
                status_code=400,
                detail=f"File type not allowed. Allowed types: {', '.join(ALLOWED_EXTENSIONS)}"
            )

        # Save the file
        file_path = os.path.join(UPLOAD_DIR, file.filename)
        with open(file_path, "wb") as buffer:
            shutil.copyfileobj(file.file, buffer)

        # Load the document into LocalLLM
        llm_instance.load_documents([file_path])
        logger.info("FINISHED CHUNKING DOCUMENT")

        return JSONResponse(
            content={
                "filename": file.filename,
                "status": "File uploaded and processed successfully",
                "file_path": file_path
            },
            status_code=200
        )

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.post("/upload-multiple/")
async def upload_multiple_files(files: List[UploadFile] = File(...)):
    uploaded_files = []
    file_paths = []
    
    try:
        for file in files:
            # Check file extension
            file_ext = os.path.splitext(file.filename)[1].lower()
            if file_ext not in ALLOWED_EXTENSIONS:
                raise HTTPException(
                    status_code=400,
                    detail=f"File type not allowed: {file.filename}"
                )

            # Save the file
            file_path = os.path.join(UPLOAD_DIR, file.filename)
            with open(file_path, "wb") as buffer:
                shutil.copyfileobj(file.file, buffer)
            
            file_paths.append(file_path)
            uploaded_files.append({
                "filename": file.filename,
                "file_path": file_path
            })

        # Load all documents into LocalLLM
        llm_instance.load_documents(file_paths)
        logger.info('FINISHED CHUNKING DOCUMENT')

        return JSONResponse(
            content={
                "message": "Files uploaded and processed successfully",
                "uploaded_files": uploaded_files
            },
            status_code=200
        )

    except Exception as e:
        # Clean up any uploaded files in case of error
        for file_info in uploaded_files:
            if os.path.exists(file_info["file_path"]):
                os.remove(file_info["file_path"])
        raise HTTPException(status_code=500, detail=str(e))
