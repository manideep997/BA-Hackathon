from fastapi import FastAPI, UploadFile, File, BackgroundTasks
from fastapi.middleware.cors import CORSMiddleware
import uvicorn
import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

app = FastAPI(title="Fill in the Frames API")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/api/health")
def health_check():
    return {"status": "ok", "service": "Backend is running"}

@app.post("/api/upload")
async def upload_dataset(file: UploadFile = File(...)):
    logger.info(f"Received file upload: {file.filename}")
    return {"filename": file.filename, "status": "uploaded"}

@app.post("/api/interpolate")
async def trigger_interpolation(background_tasks: BackgroundTasks):
    logger.info("Triggered background interpolation task")
    # Simulate background task
    return {"task_id": "mock_task_id", "status": "processing"}

@app.get("/api/status/{task_id}")
def check_status(task_id: str):
    return {"task_id": task_id, "status": "completed"}

if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)
