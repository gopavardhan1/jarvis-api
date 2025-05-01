from flask import Flask, request, jsonify
import requests
import os

app = Flask(__name__)

# Replace this with your Hugging Face API key
HUGGINGFACE_API_KEY = "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"

# Replace with any supported text generation model
MODEL_NAME = "mistralai/Mixtral-8x7B-Instruct-v0.1"

API_URL = f"https://api-inference.huggingface.co/models/{MODEL_NAME}"
HEADERS = {
    "Authorization": f"Bearer {HUGGINGFACE_API_KEY}"
}


@app.route("/ask", methods=["POST"])
def ask():
    user_question = request.form.get("question", "")
    if not user_question:
        return jsonify({"reply": "No question received."})

    payload = {
        "inputs": user_question,
        "options": {"wait_for_model": True}
    }

    try:
        response = requests.post(API_URL, headers=HEADERS, json=payload)
        response.raise_for_status()
        data = response.json()

        if isinstance(data, list) and "generated_text" in data[0]:
            reply = data[0]["generated_text"]
        elif isinstance(data, dict) and "error" in data:
            reply = f"Error: {data['error']}"
        else:
            reply = "Invalid response from Hugging Face."

    except Exception as e:
        reply = f"Error contacting Hugging Face: {str(e)}"

    return jsonify({"reply": reply})


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)
