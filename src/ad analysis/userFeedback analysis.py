import json
from transformers import pipeline
import os

# Loads the sentiment analysis model
nlp = pipeline("sentiment-analysis",
               model="distilbert-base-uncased-finetuned-sst-2-english")


def analyze_sentiment(text):
    return nlp(text)


current_directory = os.path.dirname(os.path.realpath(__file__))
json_file_path = os.path.join(
    current_directory, "../../data/feedback_data.json")

with open(json_file_path, 'r') as file:
    data = json.load(file)

for record in data:
    feedback = record['FeedbackText']
    sentiment_result = analyze_sentiment(feedback)
    print(f"Website: {record['Website_URL']}")
    print(f"Feedback: {feedback}")
    print(f"Sentiment: {sentiment_result}\n")
