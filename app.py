from flask import Flask, request, jsonify
import requests

app = Flask(__name__)

API_URL = "https://api-inference.huggingface.co/models/mistralai/Mistral-7B-Instruct-v0.1"
HF_TOKEN = "Bearer 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"

headers = {"Authorization": HF_TOKEN}

@app.route('/chat', methods=['POST'])
def chat():
    data = request.get_json()
    prompt = data.get("prompt", "")
    response = requests.post(API_URL, headers=headers, json={
        "inputs": prompt
    })
    return jsonify(response.json())

@app.route('/')
def home():
    return "JARVIS API is working!"
