# Phone Number Verification

This Python script checks the validity of phone numbers and verifies if they exist in a phonebook dataset stored in a JSON file.

## Import Statements
```python

import json
import re
import os
```
## File Path Configuration
```python

current_directory = os.path.dirname(os.path.realpath(__file__))
json_file_path = os.path.join(
    current_directory, "../../data/phonebook_data.json")
```
## Functions
### 'is_valid_phone_number'
This function uses regular expressions to check if the input is a valid phone number.

```python
def is_valid_phone_number(phone_number):
    return bool(re.match(r'^\d{3}$|^\d{4}$|^\d{10}$', phone_number))
```
### 'check_phone_number'
This function checks if the provided phone number is present in the phonebook data.

```python

def check_phone_number(phone_number, phonebook_data):
    if not is_valid_phone_number(phone_number):
        print("Invalid phone number. Please enter a valid phone number.")
        return

    for entry in phonebook_data:
        if entry['PhoneNumber'] == phone_number:
            contact_name = entry['ContactName']
            print(f"{phone_number} is legit.\nThis number belongs to {contact_name}.")
            return

    print(f"{phone_number} is suspicious.\nThis number is not present in the PhoneBook.")
```
### 'main'
This function is the main entry point of the script. It loads phonebook data from the JSON file and allows the user to check phone numbers.

```python
def main():
    json_filename = 'phonebook_data.json'
    with open(json_filename, 'r') as json_file:
        phonebook_data = json.load(json_file)

    while True:
        user_phone_number = input(
            "Enter the phone number to check (or 'exit' to stop): ")

        if user_phone_number.lower() == 'exit':
            break

        check_phone_number(user_phone_number, phonebook_data)

if __name__ == "__main__":
    main()
```
## Usage
Replace the placeholder '../../data/phonebook_data.json' with the actual path to your JSON file.
Run the script, and it will prompt you to enter phone numbers for verification.
## License
This project is licensed under the MIT License
