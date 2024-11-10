# Speech-to-Text Flask App

This is a simple Flask web application that allows users to upload audio files and receive a transcribed text version using OpenAI's Whisper model. It supports `.wav`, `.mp4`, and `.m4a` audio formats, automatically converting the audio to `.wav` format for transcription.

## Features

- Upload audio files and convert them to text using Whisper.
- Supports `.wav`, `.mp4`, and `.m4a` audio formats.
- Automatically converts `.mp4` and `.m4a` to `.wav` format.
- Download the transcription as a text file.
- The app automatically opens in the default web browser.

## Setup Instructions

### 1. Clone the repository

```bash
git clone https://github.com/kaansen97/speech-to-text-app.git
cd speech-to-text-app
```

# For Python 3.9 or later (Set up environment)

```bash
python3.9 -m venv TTS_Model_env
source TTS_Model_env/bin/activate  # On macOS or Linux
```

### 2. Install Dependencies
pip install -r requirements.txt

### 3.Install FFmpeg
On Mac :
brew install ffmpeg
On Ubuntu :
sudo apt update
sudo apt install ffmpeg

### 4. Run the Flask App
To start the Flask app, run:
python app.py

## File Structure
``` bash
speech-to-text-app/

├── app.py               # Main Flask application
├── templates/           # HTML templates
│   ├── index.html       # Upload page template
│   └── result.html      # Result page template
├── uploads/             # Directory where uploaded files are temporarily stored
├── requirements.txt     # Python dependencies
├── README.md            # This file
```
