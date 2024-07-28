from flask import render_template, request, jsonify
from app import app
from app.utils import analyze_emotion

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/detect', methods=['POST'])
def detect_emotion():
    file = request.files['file']
    emotion = analyze_emotion(file)
    return jsonify({'dominant_emotion': emotion})
