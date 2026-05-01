import os
os.environ["GRADIO_ANALYTICS_ENABLED"] = "False"

import gradio as gr
import requests
from fastapi import FastAPI

API_URL = os.getenv("API_URL", "http://api:8000/ask")

def chat(message, history):
    try:
        response = requests.post(API_URL, json={"question": message})
        return response.json().get("answer", "No response")
    except Exception as e:
        return str(e)

# Create Gradio UI
demo = gr.ChatInterface(fn=chat)

# Mount into FastAPI
app = FastAPI()
app = gr.mount_gradio_app(app, demo, path="/")