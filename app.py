from flask import Flask, request, jsonify
import requests
import os

app = Flask(__name__)

# Hugging Face API details
HF_API_TOKEN = os.getenv("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")
HF_API_URL = "https://api-inference.huggingface.co/models/mistralai/Mixtral-8x7B-Instruct-v0.1"

headers = {
    "Authorization": f"Bearer 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",
    "Content-Type": "application/json"
}

@app.route('/')
def home():
    return "Jarvis API is running!"

@app.route('/ask', methods=['POST'])
def ask():
    data = request.get_json()
    question = data.get('question')

    if not question:
        return jsonify({"reply": "No question received."})

    payload = {
        "inputs": question
    }

    response = requests.post(HF_API_URL, headers=headers, json=payload)

    if response.status_code == 200:
        output = response.json()
        if isinstance(output, list) and 'generated_text' in output[0]:
            reply = output[0]['generated_text']
        elif isinstance(output, dict) and 'generated_text' in output:
            reply = output['generated_text']
        else:
            reply = "I couldn't understand the response."
    else:
        reply = f"Error: {response.status_code}"

    return jsonify({"reply": reply})

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)
