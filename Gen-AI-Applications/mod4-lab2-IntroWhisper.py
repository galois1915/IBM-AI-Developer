#pip install git+https://github.com/openai/whisper.git

#--------- Transcription with Whisper
import whisper
# Load the Whisper model
model = whisper.load_model("base")
# Transcribe the audio file
result = model.transcribe("sample.mp3")
# Output the transcription
print(result["text"])

#---------- Whisper in applications
from flask import Flask, request
app = Flask(__name__)
model = whisper.load_model("base")
@app.route("/transcribe", methods=["POST"])
def transcribe_audio():
    audio_file = request.files["audio"]
    result = model.transcribe(audio_file)
    return {"transcription": result["text"]}
if __name__ == "__main__":
    app.run(debug=True)