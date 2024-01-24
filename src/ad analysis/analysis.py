import requests
from PIL import Image
from io import BytesIO
import pytesseract
from transformers import pipeline


def extract_text_from_image(image_url):
    response = requests.get(image_url)
    if response.status_code == 200:
        image = Image.open(BytesIO(response.content))
        text = pytesseract.image_to_string(image)
        return text
    else:
        return "Failed to retrieve the image"


nlp = pipeline("sentiment-analysis",
               model="distilbert-base-uncased-finetuned-sst-2-english")

ad_image_url = 'https://mobileads.indiatimes.com/Web_Ads/ROADBLOCK/2024/samsung/S_series/22jan24/300x250.webp'

ad_text = extract_text_from_image(ad_image_url)

if ad_text != "Failed to retrieve the image":
    sentiment_result = nlp(ad_text)
    print(f"Ad Text: {ad_text}")
    print(f"Sentiment Analysis Result: {sentiment_result}")
else:
    print(ad_text)
