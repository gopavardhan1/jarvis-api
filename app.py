from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route("/chat", methods=["POST"])
def chat():
    user_input = request.json.get("message", "")
    
    if "hi" in user_input.lower():
        reply = "Hello! How can I assist you today?"
    elif "your name" in user_input.lower():
        reply = "I am Jarvis, your AI assistant."
    else:
        reply = "I'm still learning, but I'll do my best!"
    
    return jsonify({"reply": reply})

if __name__ == "__main__":
    app.run()
