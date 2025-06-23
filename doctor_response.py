#Step1a: Setup Text to Speech–TTS–model with gTTS (keeping as backup)

import os
from gtts import gTTS

def text_to_speech_with_gtts_old(input_text, output_filepath):
    language="en"

    audioobj= gTTS(
        text=input_text,
        lang=language,
        slow=False
    )
    audioobj.save(output_filepath)


#Step1b: Setup Text to Speech–TTS–model with ElevenLabs

import os
import elevenlabs
from elevenlabs.client import ElevenLabs

ELEVENLABS_API_KEY=os.environ.get("ELEVEN_API_KEY")

def text_to_speech_with_elevenlabs_old(input_text, output_filepath):
    client=ElevenLabs(api_key=ELEVENLABS_API_KEY)
    audio=client.generate(
        text= input_text,
        voice= "Aria",  # You can change this to other voices like "Rachel", "Domi", "Bella", etc.
        output_format= "mp3_22050_32",
        model= "eleven_turbo_v2"
    )
    elevenlabs.save(audio, output_filepath)

#Step2: Use ElevenLabs for Text output to Voice automatically with playback

import subprocess
import platform
from pydub import AudioSegment
from pydub.playback import play

def text_to_speech_with_gtts(input_text, output_filepath):
    """Keeping gTTS as backup function"""
    language="en"

    audioobj= gTTS(
        text=input_text,
        lang=language,
        slow=False
    )
    audioobj.save(output_filepath)
    audio = AudioSegment.from_file(output_filepath, format="mp3")
    play(audio)

def text_to_speech_with_elevenlabs(input_text, output_filepath):
    """Main function to use ElevenLabs TTS with automatic playback"""
    try:
        client = ElevenLabs(api_key=ELEVENLABS_API_KEY)
        
        # Use the correct method for newer ElevenLabs API
        audio = client.text_to_speech.convert(
            voice_id="EXAVITQu4vr4xnSDxMaL",  # Rachel's voice ID
            text=input_text,
            model_id="eleven_turbo_v2"
        )
        
        # Save the audio file
        with open(output_filepath, "wb") as f:
            for chunk in audio:
                f.write(chunk)
        
        # Auto-play the generated audio
        audio_segment = AudioSegment.from_file(output_filepath, format="mp3")
        play(audio_segment)
        
        return output_filepath
        
    except Exception as e:
        print(f"ElevenLabs TTS failed: {e}")
        print("Falling back to gTTS...")
        # Fallback to gTTS if ElevenLabs fails. The gTTS fallback ensures your app keeps working even if you hit API limits.
        return text_to_speech_with_gtts(input_text, output_filepath)

# Alternative implementation using OS-specific audio players (if pydub.playback doesn't work)
def text_to_speech_with_elevenlabs_alt(input_text, output_filepath):
    """Alternative implementation using system audio players"""
    try:
        client = ElevenLabs(api_key=ELEVENLABS_API_KEY)
        
        # Use the correct method for newer ElevenLabs API
        audio = client.text_to_speech.convert(
            voice_id="EXAVITQu4vr4xnSDxMaL",  # Rachel's voice ID
            text=input_text,
            model_id="eleven_turbo_v2"
        )
        
        # Save the audio file
        with open(output_filepath, "wb") as f:
            for chunk in audio:
                f.write(chunk)
        
        # Play using OS-specific commands
        os_name = platform.system()
        try:
            if os_name == "Darwin":  # macOS
                subprocess.run(['afplay', output_filepath])
            elif os_name == "Windows":  # Windows
                subprocess.run(['powershell', '-c', f'(New-Object Media.SoundPlayer "{output_filepath}").PlaySync();'])
            elif os_name == "Linux":  # Linux
                subprocess.run(['aplay', output_filepath])  # Alternative: use 'mpg123' or 'ffplay'
            else:
                raise OSError("Unsupported operating system")
        except Exception as play_error:
            print(f"Audio playback failed: {play_error}")
            
        return output_filepath
        
    except Exception as e:
        print(f"ElevenLabs TTS failed: {e}")
        print("Falling back to gTTS...")
        return text_to_speech_with_gtts(input_text, output_filepath)

# Test the function
# if __name__ == "__main__":
#     input_text = "Hi, this is your AI doctor speaking with a natural voice from ElevenLabs!"
#     text_to_speech_with_elevenlabs(input_text, "elevenlabs_testing.mp3")

# Common voice IDs for ElevenLabs:
# Rachel: "EXAVITQu4vr4xnSDxMaL"
# Domi: "AZnzlk1XvdvUeBnXmlld"  
# Bella: "EXAVITQu4vr4xnSDxMaL"
# Antoni: "ErXwobaYiN019PkySvjV"
# Arnold: "VR6AewLTigWG4xSOukaG"
# Josh: "TxGEqnHWrfWFTfGW9XjX"
# Sam: "yoZ06aMxZJJ28mfd3POQ"