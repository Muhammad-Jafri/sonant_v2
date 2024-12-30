from src.services.tts import TTSService
from src.services.asr import ASRService
from src.services.llm import LLMService
from fastapi import APIRouter, HTTPException
from src.routes.agent.schemas import ChatRequest
from src.config import settings
from fastapi.responses import Response
import base64

router = APIRouter()

# Services
tts_service = TTSService(model_path=settings.TTS_MODEL_PATH)
asr_service = ASRService(model_path=settings.ASR_MODEL_PATH)
llm_service = LLMService(api_key=settings.OPENAI_API_KEY)


@router.get("/")
async def read_root():
    return {"message": "agent root"}


@router.post("/chat")
def chat_with_agent(chat_request: ChatRequest):
    """
    Chat with the agent using TTS, ASR, and LLM services.
    """
    audio_str = chat_request.audio  # Base64 encoded audio

    # Transcribe audio to text
    try:
        text = asr_service.transcribe(audio_str)
        print(f"Transcribed text: {text}")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

    # Generate response
    try:
        response = llm_service.answer_query(query=text)
        print(f"Response: {response}")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

    # Convert response to audio
    try:
        audio_response = tts_service.generate_audio(text=response)
        audio_base64 = base64.b64encode(audio_response).decode('utf-8')
        print("sending audio response back")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

    return {"audio": audio_base64}
