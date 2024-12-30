import base64
import io

import numpy as np
import soundfile as sf
from optimum.intel.openvino import OVModelForSpeechSeq2Seq
from transformers import AutoProcessor


class ASRService:
    """
    Automatic Speech Recognition service using OpenVINO-optimized Whisper model.
    """

    def __init__(self, model_path: str = "OpenVINO/whisper-medium-int8-ov",
                 sampling_rate: int = 16000):  # TODO change model to distil whisper medium for faster inference
        """
        Initialize the ASR service.

        Args:
            model_id (str): HuggingFace model ID for the Whisper model
            sampling_rate (int): Target sampling rate for audio processing
        """
        self.model_id = model_path
        self.sampling_rate = sampling_rate

        # Initialize tokenizer and model
        try:
            self.processor = AutoProcessor.from_pretrained(model_path)
            self.model = OVModelForSpeechSeq2Seq.from_pretrained(model_path)
        except Exception as e:
            raise RuntimeError(f"Failed to load model and tokenizer: {str(e)}")

    def transcribe(self, audio_base64: str) -> str:
        """
        Transcribe base64-encoded audio to text.

        Args:
            audio_base64 (str): Base64 encoded audio string

        Returns:
            str: Transcribed text

        Raises:
            ValueError: If audio conversion fails
            RuntimeError: If transcription fails
        """
        try:
            # Convert base64 to numpy array
            audio_array = self.base64_to_numpy_array(audio_base64)

            # Prepare features
            input_features = self.processor(
                audio_array,
                sampling_rate=self.sampling_rate,
                return_tensors="pt"
            ).input_features

            # Generate transcription
            outputs = self.model.generate(input_features)  # TODO fix this tomorrow

            # Decode the outputs
            transcribed_text = self.processor.batch_decode(outputs)[0]

            return transcribed_text

        except Exception as e:
            raise RuntimeError(f"Transcription failed: {str(e)}")

    @staticmethod
    def base64_to_numpy_array(base64_audio: str) -> np.ndarray:
        """
        Convert base64 encoded audio to numpy array.

        Args:
            base64_audio (str): Base64 encoded audio string

        Returns:
            np.ndarray: Audio data as numpy array

        Raises:
            ValueError: If base64 conversion fails
        """
        try:
            # Decode base64 string
            audio_bytes = base64.b64decode(base64_audio)

            # Create an in-memory binary stream
            audio_io = io.BytesIO(audio_bytes)

            # Read audio file using soundfile
            # This supports multiple formats (WAV, FLAC, OGG, etc.)
            audio_array, sample_rate = sf.read(audio_io)

            # Convert to mono if stereo
            if len(audio_array.shape) > 1:
                audio_array = audio_array.mean(axis=1)

            return audio_array

        except Exception as e:
            raise ValueError(f"Failed to convert base64 to audio array: {str(e)}")

    def __call__(self, audio_base64: str) -> str:
        """
        Make the class callable for easier use.

        Args:
            audio_base64 (str): Base64 encoded audio string

        Returns:
            str: Transcribed text
        """
        return self.transcribe(audio_base64)