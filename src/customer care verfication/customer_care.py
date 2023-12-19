import os
import json


current_directory = os.path.dirname(os.path.realpath(__file__))
json_file_path = os.path.join(
    current_directory, "../../data/number_database.json")

# Load existing database or create an empty one
try:
    with open('number_database.json', 'r') as file:
        number_database = json.load(file)
except FileNotFoundError:
    # If the file is not found, initialize an empty database
    number_database = {}


def save_database():
    # Save the current database to the JSON file
    with open('number_database.json', 'w') as file:
        json.dump(number_database, file)


def check_number(number):
    # Check if the entered number is in the database
    if number in number_database:
        # If the number is found, return  org information
        return f"Number is correct. Belongs to: {number_database[number]['org']}"
    else:
        # If the number is not found, return 'Spam'
        return "Spam"


# Example usage
while True:
    # Get user input for the number to check
    user_input = input("Enter a number to check: ")

    # Printing  the result
    result = check_number(user_input)
    print(result)
