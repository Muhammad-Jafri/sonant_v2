import wave
import base64
from piper.voice import PiperVoice
from app.utils.time_decorator import measure_time


class TTSService:
    def __init__(self, model_path: str):
        self.model_path = model_path
        self.voice = PiperVoice.load(model_path)

    @measure_time
    def generate_audio(self, text: str):
        clean_text = self.preprocess_text(text)
        temp_wav_file = wave.open("output.wav", "w")
        self.voice.synthesize(clean_text, temp_wav_file)
        temp_wav_file.close()

        with open("output.wav", "rb") as audio_file:
            audio_data = audio_file.read()
            base64_audio = base64.b64encode(audio_data).decode()

        return base64_audio

    @staticmethod
    def preprocess_text(text: str) -> str:
        # Handle empty or None input
        if not text:
            return ""

        # Step 1: Replace multiple spaces with single space
        text = ' '.join(text.split())

        import re

        # Step 2: Define punctuation marks to keep
        # Keeps: periods, commas, question marks, exclamation marks,
        # semicolons, colons, and quotation marks
        pattern = r'[^a-zA-Z0-9\s\.,!?;:"\']'

        # Remove special characters while preserving allowed punctuation
        cleaned_text = re.sub(pattern, ' ', text)

        # Step 3: Clean up any double spaces that might have been created
        cleaned_text = ' '.join(cleaned_text.split())

        # Step 4: Strip leading/trailing whitespace
        cleaned_text = cleaned_text.strip()

        return cleaned_text

    def __call__(self, *args, **kwargs):
        pass

