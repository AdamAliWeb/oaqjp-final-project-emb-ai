from flask import Flask, request, render_template
from EmotionDetection.emotion_detection import emotion_detector

app = Flask("EmotionDetectionApplication")

@app.route("/emotionDetector")
def sent_detector():
    text_to_analyze = request.args.get("textToAnalyze")

    response = emotion_detector(text_to_analyze)

    dominant_emotion = response["dominant_emotion"]
    del response["dominant_emotion"]

    message = "For the given statement, the system response is "

    for key, value in response.items():
        message += f"'{key}': {value}, "

    message = f"{message[0:-2]}. The dominant emotion is {dominant_emotion}."

    return message

@app.route("/")
def render_index_page():
    return render_template("index.html")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)