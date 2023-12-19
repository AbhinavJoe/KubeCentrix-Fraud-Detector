import os
import json


def collect_user_feedback():
    # Prompt user for website URL
    url = input("Enter the URL of the website: ")

    # Prompt user for feedback
    feedback = input("Please provide feedback for the website: ")

    # Construct the path for the JSON file
    current_directory = os.path.dirname(os.path.realpath(__file__))
    json_file_path = os.path.join(
        current_directory, "../data/UserFeedback.json")

    # Try to read existing feedback data from the JSON file
    try:
        with open(json_file_path, 'r') as json_file:
            existing_data = json.load(json_file)
    except FileNotFoundError:
        # If the file doesn't exist, create an empty dictionary
        existing_data = {}

    # Update the existing data with new feedback
    existing_data[url] = feedback

    # Writing updated data to the JSON file
    with open(json_file_path, 'w') as json_file:
        json.dump(existing_data, json_file, indent=4)

    print("Feedback successfully recorded.")


# Call the function to collect user feedback
collect_user_feedback()
