# Step 1: Setup audio recorder(ffmpeg & sounddevice)
import logging
import speech_recognition as sr
from pydub import AudioSegment
# import sounddevice as sd
from io import BytesIO

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def record_audio(file_path, timeout=10, phrase_time_limit=None):
    """
    Simplified function to record audio from the microphone and save it as an MP3 file.

    Args:
    file_path (str): Path to save the recorded audio file.
    timeout (int): Maximum time to wait for a phrase to start (in seconds).
    phrase_time_lfimit (int): Maximum time for the phrase to be recorded (in seconds).
    """
    recognizer = sr.Recognizer()
    
    try:
        with sr.Microphone() as source:
            logging.info("Adjusting for ambient noise...")
            recognizer.adjust_for_ambient_noise(source, duration=1)
            logging.info("Start speaking now...")
            
            # Record the audio
            audio_data = recognizer.listen(source, timeout=timeout, phrase_time_limit=phrase_time_limit)
            logging.info("Recording complete.")
            
            # Convert the recorded audio to an MP3 file
            wav_data = audio_data.get_wav_data()
            audio_segment = AudioSegment.from_wav(BytesIO(wav_data))
            audio_segment.export(file_path, format="mp3", bitrate="128k")
            
            logging.info(f"Audio saved to {file_path}")

            
    except Exception as e:
        logging.error(f"An error occurred: {e}")

# record_audio("patient_query.mp3")


# Setp 2: Setup Speech-to-Text STT model for audio transcription

import os
from groq import Groq

GROQ_API_KEY = os.environ.get("GROQ_API_KEY")
stt_model = "whisper-large-v3-turbo"

def transcribe_with_groq(stt_model, audio_filepath, GROQ_API_KEY):
    client = Groq(api_key=GROQ_API_KEY)

    with open(audio_filepath, "rb") as audio_file:
        transcription = client.audio.transcriptions.create(
            model=stt_model,
            file=audio_file,
            language="en"
    )

    # logging.info(f"Transcription: {transcription.text}")
    return transcription.text
    

# text = transcribe_with_groq(stt_model, "patient_query.mp3", GROQ_API_KEY)
# logging.info(f"Transcription: {text}")