import pytesseract
import requests
from PIL import Image
from io import BytesIO

# URL of the image
image_url = 'https://tpc.googlesyndication.com/simgad/1462447038842297607?'

# Fetch the image from the URL
response = requests.get(image_url)
if response.status_code == 200:
    image = Image.open(BytesIO(response.content))

    # Use Tesseract to do OCR on the image
    text = pytesseract.image_to_string(image)
    print(text)
else:
    print("Failed to retrieve the image")
