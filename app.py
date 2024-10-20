from flask import Flask, request, render_template, redirect, url_for, send_file
import whisper
import webbrowser
import os
import subprocess
from threading import Timer

app = Flask(__name__)
# Below code you can download a Large model if you want more precision but this will slow your computation
model = whisper.load_model("medium")  

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/upload', methods=['POST'])
def upload_file():
    if 'audio' not in request.files:
        return redirect(url_for('index'))
    
    file = request.files['audio']
    if file.filename == '':
        return redirect(url_for('index'))

    uploads_dir ='uploads'
    os.makedirs(uploads_dir, exist_ok=True)

    filepath = os.path.join(uploads_dir, file.filename)
    file.save(filepath) 

    if not os.path.isfile(filepath):
        return f"Error: File not found at {filepath}"

    audio_filepath = filepath  

    if filepath.endswith('.mp4') or filepath.endswith('.m4a'):
        audio_filepath = filepath.rsplit('.', 1)[0] + '.wav'
        subprocess.run(['ffmpeg', '-i', filepath, audio_filepath])
        os.remove(filepath)  
    result = model.transcribe(audio_filepath)

    transcript_file = audio_filepath + '_transcript.txt'
    with open(transcript_file, 'w') as f:
        f.write(result['text'])

    os.remove(audio_filepath)

    return render_template('result.html', transcript=result['text'], transcript_file=transcript_file)

@app.route('/download/<path:filename>', methods=['GET'])
def download_file(filename):
    return send_file(filename, as_attachment=True)

def open_browser():
    webbrowser.open_new('http://127.0.0.1:5000/')

if __name__ == '__main__':
    Timer(1, open_browser).start()
    app.run(debug=True)
