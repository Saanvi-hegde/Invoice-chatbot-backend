from fastapi import FastAPI
from app.routes import upload, chat

app = FastAPI()

@app.get("/")
def root():
    return {"message": "Backend is running"}

app.include_router(upload.router, prefix="/upload")
app.include_router(chat.router, prefix="/chat")
