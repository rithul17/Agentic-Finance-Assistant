from fastapi import FastAPI, UploadFile, File, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from starlette.responses import JSONResponse
from fastapi.responses import FileResponse
import shutil
import os
import uuid

app = FastAPI()

# Optional: enable CORS if frontend is hosted separately
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # adjust in production
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

UPLOAD_DIR = "uploads"
os.makedirs(UPLOAD_DIR, exist_ok=True)

@app.post("/upload-audio/")
async def upload_audio(file: UploadFile = File(...)):
    if file.content_type != "audio/wav":
        raise HTTPException(status_code=400, detail="Only WAV files are supported.")
    
    # Save the uploaded file
    unique_filename = f"{uuid.uuid4()}.wav"
    save_path = os.path.join(UPLOAD_DIR, unique_filename)
    
    with open(save_path, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)
    
    return JSONResponse({
        "message": "Audio file received successfully.",
        "filename": unique_filename
    })

@app.get("/get-tts-audio/")
async def get_tts_audio():
    file_path = "output.wav"  # or the full path if needed
    if not os.path.exists(file_path):
        raise HTTPException(status_code=404, detail="TTS audio not found.")
    
    return FileResponse(file_path, media_type="audio/wav", filename="output.wav")

