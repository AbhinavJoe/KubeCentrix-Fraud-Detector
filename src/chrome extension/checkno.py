import json
import re
import os

current_directory = os.path.dirname(os.path.realpath(__file__))
json_file_path = os.path.join(
    current_directory, "../../data/phonebook_data.json"
)


def is_valid_phone_number(phone_number):
    # Use a regular expression to check if the input is a valid phone number
    return bool(re.match(r'^\d{3}$|^\d{4}$||^\d{9}^\d{10}|^\d{11}}|^\d{12}$', phone_number))


def check_phone_number(phone_number, phonebook_data):
    if not is_valid_phone_number(phone_number):
        print("Invalid phone number. Please enter a valid phone number.")
        return

    # Check if the phone number is present in the JSON data
    for entry in phonebook_data:
        if entry['PhoneNumber'] == phone_number:
            contact_name = entry['ContactName']
            print(f"{phone_number} is legit\nThis number belongs to {contact_name}.")
            return

    # If the phone number is not found in the JSON data
    print(f"{phone_number} is suspicious.\nThis number is not present in the PhoneBook.")


def main():
    # Load data from the JSON file
    with open(json_file_path, 'r') as json_file:
        phonebook_data = json.load(json_file)

    while True:
        # Take user input for the phone number
        user_phone_number = input(
            "Enter the phone number to check (or 'exit' to stop): ")

        # Check if the user wants to exit
        if user_phone_number.lower() == 'exit':
            break

        # Check the phone number
        check_phone_number(user_phone_number, phonebook_data)


if __name__ == "__main__":
    main()
