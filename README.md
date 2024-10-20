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
git clone https://github.com/yourusername/speech-to-text-app.git
cd speech-to-text-app
