# Sonant

Sonant is a comprehensive end-to-end speech solution designed to enable seamless conversations with large language models (LLMs). It provides a robust framework for speech-to-text, text-to-speech, and conversational AI integration, empowering developers to create natural and intuitive voice-driven applications.

---

## Features
- **Speech-to-Text**: High-accuracy transcription for seamless voice input, powered by Distil Small EN.
- **Text-to-Speech**: Realistic and expressive speech output using Piper TTS for fast generation.
- **LLM Integration**: Connects directly with language models to enable dynamic and context-aware interactions.
- **Customizable**: Configure and extend functionalities to suit your specific use case.
- **CPU Optimized**: Designed to perform efficiently in CPU-based environments.

---

## Requirements
- Python 3.11 or higher.
- Uvicorn (for running the server).

---

## Setup Instructions
You can set up Sonant using either **Dev Containers** or a **Virtual Environment**.

### Option 1: Dev Containers
1. Ensure you have Docker and a compatible IDE (e.g., VS Code) installed.
2. Open the project in VS Code.
3. Follow the prompt to reopen the folder in the dev container.
4. The dev container setup will handle dependencies and environment setup for you.

### Option 2: Virtual Environment
1. **Create a Virtual Environment**:
   ```bash
   python3.11 -m venv venv
   ```
2. **Activate the Virtual Environment**:
   - On Linux/MacOS:
     ```bash
     source venv/bin/activate
     ```
   - On Windows:
     ```cmd
     venv\Scripts\activate
     ```
3. **Install Dependencies**:
   ```bash
   pip install -r requirements.txt
   ```
4. **Environment Variables**:
   - Add your API key in the `.env.example` file.
   - Copy the `.env.example` file to create a `.env` file:
     ```bash
     cp .env.example .env
     ```
   - Ensure the `.env` file is correctly filled with the required configuration.

5. **Download TTS Model**:
   - Use the TTS model "en_alba_medium.onnx" for Piper TTS. Download it from the following link: [Piper Voices](https://github.com/rhasspy/piper/blob/master/VOICES.md).
   - Place the file in ml_models/tts_model

---

## Running the Server
Start the application server using the following command:
```bash
uvicorn src.main:app --reload
```

---

## Contributing
We welcome contributions to Sonant! Please fork the repository and create a pull request for any changes or improvements.

---

## License
Sonant is licensed under [MIT License](LICENSE).

---

## Contact
For questions or support, please reach out to [your email/contact info].

