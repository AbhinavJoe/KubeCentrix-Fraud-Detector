# Image Text Extraction and Sentiment Analysis

This script retrieves an image from a given URL, extracts text from the image using OCR (Optical Character Recognition), and then performs sentiment analysis on the extracted text using a pre-trained DistilBERT model fine-tuned for sentiment analysis.

## Requirements

- Python 3.x
- Libraries:
  - `requests`
  - `PIL` (Python Imaging Library)
  - `pytesseract`
  - `transformers`

## Usage

1. Import required libraries:
    ```python
    import requests
    from PIL import Image
    from io import BytesIO
    import pytesseract
    from transformers import pipeline
    ```

2. Define the function `extract_text_from_image(image_url)` to extract text from the given image URL using Tesseract OCR:
    ```python
    def extract_text_from_image(image_url):
        response = requests.get(image_url)
        if response.status_code == 200:
            image = Image.open(BytesIO(response.content))
            text = pytesseract.image_to_string(image)
            return text
        else:
            return "Failed to retrieve the image"
    ```

3. Initialize a sentiment analysis pipeline using the DistilBERT model:
    ```python
    nlp = pipeline("sentiment-analysis",
                   model="distilbert-base-uncased-finetuned-sst-2-english")
    ```

4. Provide the URL of the image containing the advertisement:
    ```python
    ad_image_url = 'https://mobileads.indiatimes.com/Web_Ads/ROADBLOCK/2024/samsung/S_series/22jan24/300x250.webp'
    ```

5. Extract text from the image and perform sentiment analysis:
    ```python
    ad_text = extract_text_from_image(ad_image_url)

    if ad_text != "Failed to retrieve the image":
        sentiment_result = nlp(ad_text)
        print(f"Ad Text: {ad_text}")
        print(f"Sentiment Analysis Result: {sentiment_result}")
    else:
        print(ad_text)
    ```

## Output

- If the image is retrieved successfully and text is extracted, the script prints the extracted text and the sentiment analysis result.
- If the image retrieval fails, an error message is printed indicating the failure to retrieve the image.

## Additional Notes

- Ensure that Tesseract OCR is properly configured and installed for accurate text extraction from images.
- The sentiment analysis model used in this script is a pre-trained DistilBERT model fine-tuned for sentiment analysis on English text data.

## License

This script is licensed under the MIT License.
