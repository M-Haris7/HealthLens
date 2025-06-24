# HealthLens – AI Doctor with Vision & Voice

**MediVoice** is an educational chatbot that combines speech, image understanding, and cutting‑edge LLMs to simulate a concise doctor‑style reply.

> **Disclaimer** ‑ This project is **for learning and demonstration only**. It does **not** provide real medical advice. Always consult a qualified professional.

---

## ✨ Demo

Try it live on **Hugging Face Spaces → https://huggingface.co/spaces/ThatITGuy/AI-medical-chatbot**

If the above link doesn't work try **→ https://web-production-533df.up.railway.app/**

![WhatsApp Image 2025-06-23 at 21 28 01_59cb12d1](https://github.com/user-attachments/assets/3ffb7ca2-3692-459c-aefd-2c3f23c4187b)

---

## Architecture of the app

![image](https://github.com/user-attachments/assets/7e46ad26-88da-4c94-880b-4ceee45c4d51)

---


## 🔑 Key Features

| Capability              | Details                                                                                             |
| ----------------------- | --------------------------------------------------------------------------------------------------- |
| **Voice query**         | Record directly in the browser with **Gradio** or upload an audio file (MP3/WAV).                   |
| **Image analysis**      | Upload a skin/medical photo; processed by **Llama 4‑Maverick 17B** (Groq) multimodal model.         |
| **Doctor‑style answer** | System prompt instructs the LLM to respond like a concise doctor (≤ 2 sentences, no bullet points). |
| **Realistic TTS**       | Response is spoken back using **ElevenLabs** voice (default: *Aria*).                               |
| **Web app**             | Clean Gradio UI ready for Hugging Face Spaces or local run.                                         |

---

## 🏗️ Tech Stack

| Layer          | Tech                                                                |
| -------------- | ------------------------------------------------------------------- |
| UI             | **Gradio 4+**                                                       |
| Speech‑to‑Text | **Whisper Large‑v3 Turbo(OpenAI)** via Groq API                             |
| Image + Text   | **meta‑llama/llama‑4‑maverick‑17b‑128e‑instruct** via Groq Chat API |
| Text‑to‑Speech | **ElevenLabs & Google Text to Speech** SDK                                                  |
| Audio utils    | **pydub**, **ffmpeg**                                               |
| Packaging      | `requirements.txt` (for Spaces) • optional **pipenv** locally       |

---

## 🚀 Quick Start (Local)

```bash
# 1. clone
$ git clone https://github.com/your‑username/medivoice.git && cd medivoice

# 2. install deps (choose one)
$ pip install -r requirements.txt                # classic
# OR
$ pipenv install && pipenv shell                 # pipenv workflow

# 3. set secrets (PowerShell / Bash)
$ export GROQ_API_KEY=xxxxxxxxxxxxxxxxxxxxxxxxxxxx
$ export ELEVEN_API_KEY=xxxxxxxxxxxxxxxxxxxxxxxxxx

# 4. run
$ python app.py
```

Navigate to **[http://127.0.0.1:7860](http://127.0.0.1:7860)** and test!

---

## ☁️ Deploy to Hugging Face Spaces

1. Create a **Gradio → Python** Space.
2. Add your secrets in the **ℹ️ Secrets** tab:

   * `GROQ_API_KEY`
   * `ELEVEN_API_KEY`
3. Push the repo contents (ensure **`app.py`** and **`requirements.txt`** are in the root):

   ```bash
   git lfs install
   git remote add space https://huggingface.co/spaces/your‑username/medivoice
   git push space main
   ```
4. Wait for the build → your Space URL is live!

---

## 🗂️ Project Structure

```text
medivoice/
├─ app.py                # Gradio entry‑point (HF Spaces runs this)
├─ doctor.py             # image → text with Groq LLM
├─ patient_query.py      # whisper STT helper
├─ doctor_response.py    # ElevenLabs TTS helper
├─ requirements.txt      # production deps (no PortAudio!)
└─ README.md
```

---

## 📜 License

This repository is released under the **MIT License**. See `LICENSE` for details.

---

## 🙏 Acknowledgements

* **Groq** for low‑latency LLM & Whisper APIs
* **ElevenLabs** for lifelike voices
* **Gradio** + **Hugging Face** for easy hosting
* All open‑source contributors
