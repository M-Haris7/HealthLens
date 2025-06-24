# if you dont use pipenv uncomment the following:
# from dotenv import load_dotenv
# load_dotenv()

#VoiceBot UI with Gradio
import os
import gradio as gr

from doctor import encoded_image, analyze_image_with_query
from patient_query import record_audio, transcribe_with_groq
from doctor_response import text_to_speech_with_elevenlabs  # Changed from gtts to elevenlabs


system_prompt="""You have to act as a professional doctor, i know you are not but this is for learning purpose. 
            What's in this image?. Do you find anything wrong with it medically? 
            If you make a differential, suggest some remedies for them. Donot add any numbers or special characters in 
            your response. Your response should be in one long paragraph. Also always answer as if you are answering to a real person.
            Donot say 'In the image I see' but say 'With what I see, I think you have ....'
            Dont respond as an AI model in markdown, your answer should mimic that of an actual doctor not an AI bot, 
            Keep your answer concise (max 2 sentences). No preamble, start your answer right away please"""


def process_inputs(audio_filepath, image_filepath):
    speech_to_text_output = transcribe_with_groq(GROQ_API_KEY=os.environ.get("GROQ_API_KEY"), 
                                                 audio_filepath=audio_filepath,
                                                 stt_model="whisper-large-v3-turbo")

    # Handle the image input
    if image_filepath:
        doctor_response = analyze_image_with_query(query=system_prompt+speech_to_text_output, 
                                                 encoded_image=encoded_image(image_filepath), 
                                                 model="meta-llama/llama-4-maverick-17b-128e-instruct")
    else:
        doctor_response = "No image provided for me to analyze"

    # Use ElevenLabs TTS instead of gTTS
    audio_filepath = text_to_speech_with_elevenlabs(input_text=doctor_response, 
                                                   output_filepath="final.mp3") 

    return speech_to_text_output, doctor_response, audio_filepath


# Create the interface
iface = gr.Interface(
    fn=process_inputs,
    inputs=[
        gr.Audio(sources=["microphone", "upload"], type="filepath",
                 label="Ask your query (voice)"),
        gr.Image(type="filepath")
    ],
    outputs=[
        gr.Textbox(label="Speech to Text"),
        gr.Textbox(label="Doctor's Response"),
        gr.Audio(label="Doctor's Voice Response")
    ],
    title="AI Doctor with Vision & Voice (ElevenLabs)"
)

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 7860))
    iface.launch(server_name="0.0.0.0", server_port=port, share=False, debug=False)

# http://127.0.0.1:7860
