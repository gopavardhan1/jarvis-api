from flask import Flask, request, jsonify
import requests

app = Flask(__name__)

# Replace this with your actual Hugging Face token
HUGGINGFACE_API_KEY = "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"

@app.route('/')
def home():
    return "Jarvis AI API is Live!"

@app.route('/ask', methods=['POST'])
def ask():
    data = request.get_json()
    question = data.get("question", "")

    if not question:
        return jsonify({"reply": "No question received."})

    headers = {
        "Authorization": f"Bearer {HUGGINGFACE_API_KEY}"
    }

    payload = {
        "inputs": question
    }

    response = requests.post(
        "https://api-inference.huggingface.co/models/google/flan-t5-small",
        headers=headers,
        json=payload
    )

    if response.status_code == 200:
        generated_text = response.json()[0].get("generated_text", "No response")
        return jsonify({"reply": generated_text})
    else:
        return jsonify({"reply": "Error connecting to Hugging Face"}), 500

if __name__ == '__main__':
    app.run(debug=True)
