import requests  # Import the requests library to handle HTTP requests
import json

def emotion_detector(text_to_analyse):  # Define a function named sentiment_analyzer that takes a string input (text_to_analyse)
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'  # URL of the emotion detection service
    myobj = { "raw_document": { "text": text_to_analyse } }  # Create a dictionary with the text to be analyzed
    header = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}  # Set the headers required for the API request
    response = requests.post(url, json = myobj, headers=header)  # Send a POST request to the API with the text and headers
    # Convert to json
    json_response = json.loads(response.text)
    # Create emotion score
    formatted_response = json_response["emotionPredictions"][0]["emotion"]
    # Find dominant emotion and amand to formatted_response
    dominant_emotion = max(formatted_response, key=formatted_response.get)
    formatted_response["dominant_emotion"] = dominant_emotion
    return formatted_response  # Return the response text from the API