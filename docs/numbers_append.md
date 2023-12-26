# Customer Care Number Extraction and JSON Generation

This Python script extracts customer care service names and customer care numbers from a given text format and creates a JSON file containing the data.

## Script Overview

The script takes a predefined list text and parses it to extract customer care service names and customer care numbers. It then creates a JSON file with the extracted data.

## Usage

1. Provide the list text in the specified format.

```plaintext
Airtel – 18001030405
Air India – 1800 22 7722
... (more entries)
```

2. Run the script to generate a JSON file.

## Code Explanation

- The script uses regular expressions to match and extract customer care services names and customer care numbers from each line of the provided text.

- The extracted data is stored in a list of dictionaries, where each dictionary represents a customer care service with its name and number.

- The script then creates a JSON file and writes the extracted data to it.

## Running the Script

```bash
python banks_append.py
```

## Output

The script will generate a JSON file named phonebook_data.json containing the extracted bank data. The output JSON file will have entries structured as follows:

```json
[
  {
    "ContactName": "Airtel",
    "PhoneNumber": "18001030405"
  },
  {
    "ContactName": "Air India",
    "PhoneNumber": "1800 22 7722"
  }
]
```

## Example

For example, the input line:

```plaintext
Airtel – 18001030405
```

will be converted to the following JSON entry:

```json
[
  {
    "ContactName": "Airtel",
    "PhoneNumber": "18001030405"
  }
]
```

## File Structure

1. `phonebook_generator.py`: Python script for generating phonebook data.
2. `data/phonebook_data.json`: Output JSON file with contact names and phone numbers.

## Dependencies

1. Python 3.12
2. re (regular expression) module
3. json module

## License

This script is provided under the MIT License.
