import requests
import json

def emotion_detection(text_to_analyse):
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    headers = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    myobje = { "raw_document": { "text": text_to_analyse } }
    response = requests.post(url, json=myobje, headers=headers)
    formatted_response = json.loads(response.text)

    if response.status_code == 200:
        # modified
        formatted_response = formatted_response['emotionPredictions'][0]['emotion']
        sentiments = list(formatted_response.keys())
        values = list(formatted_response.values())
        index_max = values.index(max(values))
        formatted_response['dominant_emotion'] = sentiments[index_max]
    elif response.status_code == 400:
        formatted_response = None

    return formatted_response
