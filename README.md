# DOBI 🤖

DOBI is a simple, beginner-friendly AI chatbot with a custom-built chat interface. It uses a Flask backend to securely talk to the Groq API (keeping your API key off the client) and a lightweight HTML/CSS/JS frontend for the chat window.

## Features
- 💬 Real-time chat interface with typing indicator
- 🎨 Custom-designed dark UI with a personalized avatar
- 🔒 API key stays server-side (never exposed to the browser)
- 🔄 Reset chat button to start fresh
- ⚡ Powered by Groq's fast LLM inference

## Tech Stack
- **Backend:** Python, Flask
- **Frontend:** HTML, CSS (Tailwind), JavaScript
- **AI:** Groq API (OpenAI-compatible)

## Setup

1. Clone the repo and install dependencies:
   ```bash
   pip install flask openai python-dotenv
   ```

2. Create your own `.env` file (copy the example and fill in your key):
   ```bash
   cp .env.example .env
   ```
   Then open `.env` and paste in your Groq API key:
   ```
   GROQ_API_KEY=your-actual-key-here
   ```

3. Run the app:
   ```bash
   python app.py
   ```

4. Open your browser to `http://127.0.0.1:5000`

> ⚠️ **Never commit your `.env` file.** It's already listed in `.gitignore` so git won't track it.

## Project Structure
```
dobi_app/
├── app.py                  # Flask backend
├── .env                    # Your secret API key (git-ignored, not committed)
├── .env.example            # Template showing required env vars
├── .gitignore
├── static/
│   └── dobi-avatar.png     # Chat avatar
└── templates/
    └── index.html          # Chat UI
```

## Notes
- Get a free API key at [console.groq.com](https://console.groq.com)
- This is a beginner project built for learning purposes — feel free to fork and extend it!
