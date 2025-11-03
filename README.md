# 🎙️ Jarvis AI Assistant

Jarvis is a **voice-controlled AI assistant** built with Python that integrates **speech recognition**, **text-to-speech**, and **Gemini AI** for intelligent, conversational responses. It can perform tasks like opening websites, playing music, and launching applications — all through voice commands.

---

## 🚀 Features

* 🎧 Real-time **speech recognition** and **text-to-speech**
* 💬 **Gemini AI integration** for smart, context-aware responses
* 🎵 Play, stop, next, and previous **music controls**
* 🌐 Open popular **websites and applications** by voice
* 🧠 Modular structure (`main.py`, `gemini_api.py`) for scalability
* 🔐 Secure API key handling using **dotenv**

---

## 🧩 Tech Stack

* **Python 3**
* **pyttsx3** – Text-to-speech engine
* **SpeechRecognition** + **PyAudio** – Voice input
* **google-genai** – Gemini API integration
* **python-dotenv** – Environment variable management
* **datetime**, **webbrowser**, **os**

---

## 📁 Project Structure

```
├── main.py
├── gemini_api.py
├── requirements.txt
└── .env
```

---

## ⚙️ Installation

1. **Clone the repository**

   ```bash
   git clone https://github.com/your-username/jarvis-ai-assistant.git
   cd jarvis-ai-assistant
   ```

2. **Install dependencies**

   ```bash
   pip install -r requirements.txt
   ```

3. **Set up environment variables**
   Create a `.env` file and add your Gemini API key:

   ```
   GEMINI_API_KEY=your_api_key_here
   ```

4. **Run the assistant**

   ```bash
   python main.py
   ```

---

## 🗣️ Example Commands

* “Play music”
* “Next music” / “Previous music” / “Stop music”
* “Open YouTube” / “Open Google” / “Open GitHub”
* “What’s the time?”
* “Stop Jarvis”

---

## 🔮 Future Enhancements

* Add weather, news, and email integration
* Include GUI version
* Enable offline mode
