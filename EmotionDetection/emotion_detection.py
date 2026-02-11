import requests, json

def emotion_detector(text_to_analyse):
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    header = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    myobj = { "raw_document": { "text": text_to_analyse } }

    response = requests.post(url, json=myobj, headers=header)

    formatted_response = json.loads(response.text)
    emotion_scores = "Something went wrong! Please try again."

    if response.status_code == 200:
        emotion_scores = formatted_response["emotionPredictions"][0]["emotion"]
        highest_score = 0
        dominant_emotion = ""

        for key, value in emotion_scores.items():
            if value > highest_score:
                dominant_emotion = key
                highest_score = value

        emotion_scores["dominant_emotion"] = dominant_emotion
    elif response.status_code == 400:
        emotion_scores = {
            "anger": None,
            "disgust": None, 
            "fear": None, 
            "joy": None, 
            "sadness": None, 
            "dominant_emotion": None
        }

    return emotion_scores