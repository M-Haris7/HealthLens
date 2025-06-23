# Step 1: Setup Groq API key

import os
GROQ_API_KEY = os.getenv("GROQ_API_KEY")

# Setp 2: Convert Image to required format

import base64

# image_path = "acne.jpeg"
# image_file = open(image_path, "rb")
# encoded_image = base64.b64encode(image_file.read()).decode("utf-8")

def encoded_image(image_path):   
    image_file=open(image_path, "rb")
    return base64.b64encode(image_file.read()).decode('utf-8')

# Step 3: Setup Multimodal LLM

from groq import Groq

client = Groq()
model = "meta-llama/llama-4-maverick-17b-128e-instruct"
query = "Is there something wrong with my skin? How can I treat it?"

def analyze_image_with_query(query, model, encoded_image):
    client=Groq()  
    messages=[
        {
            "role": "user",
            "content": [
                {
                    "type": "text", 
                    "text": query
                },
                {
                    "type": "image_url",
                    "image_url": {
                        "url": f"data:image/jpeg;base64,{encoded_image}",
                    },
                },
            ],
        }]
    chat_completion=client.chat.completions.create(
        messages=messages,
        model=model
    )

    return chat_completion.choices[0].message.content