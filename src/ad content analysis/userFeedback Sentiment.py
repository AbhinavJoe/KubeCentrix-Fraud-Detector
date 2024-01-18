import json
from transformers import pipeline
import os

# Load the sentiment analysis model
nlp = pipeline("sentiment-analysis",
               model="distilbert-base-uncased-finetuned-sst-2-english")

# Function to perform sentiment analysis


def analyze_sentiment(text):
    return nlp(text)


# Load the JSON file
current_directory = os.path.dirname(os.path.realpath(__file__))
json_file_path = os.path.join(
    current_directory, "../../data/feedback_data.json")  # Replace with your JSON file path

with open(json_file_path, 'r') as file:
    data = json.load(file)

# Assuming the JSON file contains a list of records
# If it's a single record, you can directly access data['FeedbackText']
for record in data:
    feedback = record['FeedbackText']
    sentiment_result = analyze_sentiment(feedback)
    print(f"Website: {record['Website_URL']}")
    print(f"Feedback: {feedback}")
    print(f"Sentiment: {sentiment_result}\n")
