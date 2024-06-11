"""
Importing libraries
"""
from flask import Flask, render_template, request
from EmotionDetection.emotion_detection import emotion_detection

app = Flask("Emotion Detector")

@app.route('/emotionDetector')
def sent_analyzer():
    """
    function to detect the emotion
    """
    text_to_analize = request.args.get('textToAnalyze')
    response = emotion_detection(text_to_analize)

    if response is None:
        return  "Invalid text! Please try again"
    return response

@app.route('/')
def render_index_template():
    """
    show template index
    """
    return render_template('index.html')

if __name__=="__main__":
    app.run(host="0.0.0.0", port=5000)
