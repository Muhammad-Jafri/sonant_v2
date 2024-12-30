from pydantic import BaseModel

class ChatRequest(BaseModel):
    audio: str # This is a base64 encoded string
    user_id: str
    
    