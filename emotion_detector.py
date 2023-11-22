import requests
import json

def emotion_detector(text_to_analyse):
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    myobj = { "raw_document": { "text": text_to_analyse } }
    header = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    response = requests.post(url, json=myobj, headers=header)
    response_dict = json.loads(response.text)
    emotion_predictions = response_dict.get("emotionPredictions", [])
    emotion_scores = {
        'anger': 0,
        'disgust': 0,
        'fear': 0,
        'joy': 0,
        'sadness': 0,
    }

    for prediction in emotion_predictions:
        emotion = prediction.get("emotion", {})
        for key, value in emotion.items():
            emotion_scores[key] += value

    dominant_emotion = max(emotion_scores, key=emotion_scores.get)

    output_dict = {
        'anger': emotion_scores['anger'],
        'disgust': emotion_scores['disgust'],
        'fear': emotion_scores['fear'],
        'joy': emotion_scores['joy'],
        'sadness': emotion_scores['sadness'],
        'dominant_emotion': dominant_emotion,
    }

    return output_dict