# Feedback Sentiment Analysis

This script analyzes the sentiment of feedback texts stored in a JSON file using a pre-trained DistilBERT model fine-tuned for sentiment analysis. It demonstrates how to load a sentiment analysis model using the `transformers` library, read data from a JSON file, and apply the model to each feedback text to determine its sentiment.

## Requirements

- Python 3.x
- Libraries:
  - `json`
  - `transformers`
  - `os`

## Usage

1. **Import Required Libraries**: Ensure that you have imported necessary Python libraries:
    ```python
    import json
    from transformers import pipeline
    import os
    ```

2. **Load the Sentiment Analysis Model**: Initialize a sentiment analysis pipeline with the DistilBERT model:
    ```python
    nlp = pipeline("sentiment-analysis", model="distilbert-base-uncased-finetuned-sst-2-english")
    ```

3. **Define the `analyze_sentiment` Function**: This function takes a text string as input and returns the sentiment analysis result using the loaded model:
    ```python
    def analyze_sentiment(text):
        return nlp(text)
    ```

4. **Set the Path to the JSON File**: Calculate the path to the JSON file that contains the feedback data. The JSON file should be structured with records that include a `Website_URL` and `FeedbackText` for each piece of feedback:
    ```python
    current_directory = os.path.dirname(os.path.realpath(__file__))
    json_file_path = os.path.join(current_directory, "../../data/feedback_data.json")
    ```

5. **Load and Analyze Feedback Data**: Open the JSON file, load the feedback data, and analyze the sentiment of each feedback text:
    ```python
    with open(json_file_path, 'r') as file:
        data = json.load(file)

    for record in data:
        feedback = record['FeedbackText']
        sentiment_result = analyze_sentiment(feedback)
        print(f"Website: {record['Website_URL']}")
        print(f"Feedback: {feedback}")
        print(f"Sentiment: {sentiment_result}\n")
    ```

## Output

- The script outputs the website URL, the original feedback text, and the sentiment analysis result for each record in the JSON file.
- The sentiment analysis result includes the label (e.g., POSITIVE or NEGATIVE) and a confidence score.

## Additional Notes

- Ensure the JSON file is correctly formatted and accessible at the specified path.
- The `transformers` library must be installed and properly configured to use the sentiment analysis model.
- This script assumes the JSON file has a specific structure. Adjust the script accordingly if your JSON structure differs.

## License

This script is licensed under the MIT License.
