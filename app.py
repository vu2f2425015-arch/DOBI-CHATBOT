"""
DOBI - Flask backend
---------------------
Serves the chat UI and securely proxies messages to the Groq API.
The API key stays on the server and is never exposed to the browser.

Setup:
1. pip install flask openai
2. Set your key:  export GROQ_API_KEY="your-key-here"
3. Run:  python app.py
4. Open: http://127.0.0.1:5000
"""

import os
from flask import Flask, render_template, request, jsonify
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()  # loads variables from a local .env file (not committed to git)

app = Flask(__name__)

GROQ_API_KEY = os.environ.get("GROQ_API_KEY")
GROQ_BASE_URL = "https://api.groq.com/openai/v1"
MODEL_NAME = "openai/gpt-oss-120b"  # Groq's current general-purpose model

if not GROQ_API_KEY:
    raise ValueError(
        "GROQ_API_KEY not found. Create a .env file with GROQ_API_KEY=your-key-here"
    )

SYSTEM_PROMPT = (
    "You are DOBI, a friendly, helpful, and slightly witty AI assistant. "
    "You keep answers clear and concise, and you're always encouraging. "
    "If you don't know something, admit it honestly."
)

client = OpenAI(api_key=GROQ_API_KEY, base_url=GROQ_BASE_URL)

# Simple in-memory conversation history (single user, resets on server restart)
conversation_history = [{"role": "system", "content": SYSTEM_PROMPT}]


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/api/chat", methods=["POST"])
def chat():
    data = request.get_json(force=True)
    user_message = (data.get("message") or "").strip()

    if not user_message:
        return jsonify({"error": "Empty message"}), 400

    conversation_history.append({"role": "user", "content": user_message})

    try:
        response = client.chat.completions.create(
            model=MODEL_NAME,
            messages=conversation_history,
            max_tokens=500,
        )
        reply = response.choices[0].message.content
        conversation_history.append({"role": "assistant", "content": reply})
        return jsonify({"reply": reply})

    except Exception as e:
        return jsonify({"error": f"Groq API error: {str(e)}"}), 500


@app.route("/api/reset", methods=["POST"])
def reset():
    global conversation_history
    conversation_history = [{"role": "system", "content": SYSTEM_PROMPT}]
    return jsonify({"status": "ok"})


if __name__ == "__main__":
    app.run(debug=True, port=5000)
