from fastapi import APIRouter
from pydantic import BaseModel

router = APIRouter(prefix="/chat", tags=["Chatbot"])

class ChatRequest(BaseModel):
    query: str

@router.post("/")
def chatbot_response(chat: ChatRequest):
    return {"response": f"AI Response to: {chat.query}"}
 
