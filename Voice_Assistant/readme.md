# Voice-Activated Personal Assistant

A Python-based voice assistant that performs tasks like checking weather, reading news, and setting reminders using speech recognition and text-to-speech.

## Features

- 🎤 **Voice Input** – Listen to user commands via microphone
- 🔊 **Voice Output** – Responds using macOS `say` command (offline, reliable)
- ⛅ **Weather Check** – Fetches current temperature and wind speed for any city (free API, no key required)
- 📰 **News Headlines** – Reads top BBC news headlines (free RSS feed)
- ⏰ **Reminders** – Set reminders with time; assistant speaks when time arrives

## Tech Stack

- `speech_recognition` – Convert speech to text (Google API)
- `requests` – Fetch weather and news data
- macOS `say` command – Text-to-speech (built-in)
- JSON – Persistent reminder storage

## Setup & Installation

### Prerequisites
- Python 3.7 or higher
- macOS (for `say` command; for Windows/Linux you'd need alternative TTS)

### Installation Steps

1. **Clone or download** this project folder.

2. **Open Terminal** in the project root directory.

3. **Install required Python libraries**:
   ```bash
   pip3 install -r requirements.txt