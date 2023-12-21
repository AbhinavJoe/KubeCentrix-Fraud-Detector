# Phone Number Database Check Python Script

This Python script is designed to check whether a given phone number is present in a database. The script utilizes a JSON file to store and retrieve information about phone numbers.

## File Paths

The script assumes a directory structure and attempts to locate the JSON file for the number database. Adjust the `json_file_path` variable if needed.

```python
import os
import json


current_directory = os.path.dirname(os.path.realpath(__file__))
json_file_path = os.path.join(
    current_directory, "../../data/number_database.json")
Loading or Initializing Database
The script tries to load an existing JSON database file (number_database.json). If the file is not found, it initializes an empty database.
```
## Loading or Initializing Database
The script tries to load an existing JSON database file (number_database.json). If the file is not found, it initializes an empty database.
```python
try:
    with open('number_database.json', 'r') as file:
        number_database = json.load(file)
except FileNotFoundError:
    number_database = {}
```
## Functions
### 'save_database'
Saves the current state of the database to the JSON file.

```python
def save_database():
    with open('number_database.json', 'w') as file:
        json.dump(number_database, file)
```
### 'check_numbers'
Checks if a given number is present in the database. If found, it returns the organization information; otherwise, it indicates the number is spam.

```python
def check_number(number):
    if number in number_database:
        return f"Number is correct. Belongs to: {number_database[number]['org']}"
    else:
        return "Spam"
```
## Example Usage

The script includes a simple example usage within a loop to continuously prompt the user for a number to check.

```python
while True:
    user_input = input("Enter a number to check: ")
    result = check_number(user_input)
    print(result)
```
## License
This script is provided under the MIT License.
