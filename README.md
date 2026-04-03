# 🤖 Jarvis - AI Voice Assistant

A Python-based voice assistant inspired by Iron Man's J.A.R.V.I.S. It listens for your voice, understands your commands, and responds accordingly.

## ✨ Features

- 🎙️ **Wake Word Detection** - Activates on saying *"Jarvis"*
- 🌐 **Open Websites** - Opens YouTube, Google, and ChatGPT on command
- 🎵 **Play Music** - Plays songs directly from YouTube
- 📰 **Latest News** - Reads out the latest news headlines
- 🤖 **OpenAI Integration** - Powered by GPT-3.5 Turbo for smart responses

## 🎵 Music Library

| Command | Song |
|--------|------|
| `play perfect` | Perfect - Ed Sheeran |
| `play believer` | Believer - Imagine Dragons |
| `play udariya` | Udariya |
| `play jinda` | Jinda |
| `play khat` | Khat |

## 🗣️ Voice Commands

| Command | Action |
|--------|--------|
| `open youtube` | Opens YouTube |
| `open google` | Opens Google |
| `open assistant` | Opens ChatGPT |
| `play <song name>` | Plays a song |
| `news` | Reads latest news headlines |

## 🛠️ Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/amanverma123-prog/jarvis.git
   cd jarvis
   ```

2. **Create a virtual environment**
   ```bash
   python -m venv .venv
   .venv\Scripts\activate
   ```

3. **Install dependencies**
   ```bash
   pip install speechrecognition pyttsx3 requests openai python-dotenv
   ```

4. **Create a `.env` file** in the root folder:
   ```
   NEWS_API_KEY=your_news_api_key_here
   ```

5. **Run Jarvis**
   ```bash
   python main.py
   ```

## 🔑 API Keys Required

- [NewsAPI](https://newsapi.org/) - For fetching news headlines
- [OpenAI](https://platform.openai.com/) - For GPT-3.5 Turbo integration

## 📁 Project Structure

```
jarvis/
├── main.py          # Main voice assistant logic
├── client.py        # OpenAI GPT integration
├── musicLibrary.py  # Music links dictionary
├── .gitignore       # Files to ignore in Git
└── README.md        # Project documentation
```

## 🚀 Usage

1. Run `main.py`
2. Wait for *"Initializing Jarvis..."*
3. Say **"Jarvis"** to activate
4. Give your command!

---

Made with ❤️ by [Aman Verma](https://github.com/amanverma123-prog)
