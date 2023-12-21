# Bank Data Extraction and JSON Generation

This Python script extracts bank names and URLs from a given text format and creates a JSON file containing the bank data.

## Script Overview

The script takes a predefined bank list text and parses it to extract bank names and URLs. It then creates a JSON file with the extracted data.

## Usage

1. Provide the bank list text in the specified format.

   ```plaintext
   Abhyudaya Co-op Bank    www.abhyudaya.com
   Abu Dhabi Commercial Bank    www.adcb.com
   Ahmedabad Mercantile Co-op Bank    www.amco-bank.com
   # ... (add all other banks)
   ```

2. Run the script to generate a JSON file.

## Code Explanation

- The script uses regular expressions to match and extract bank names and URLs from each line of the provided text.

- The extracted data is stored in a list of dictionaries, where each dictionary represents a bank with its name and URL.

- The script then creates a JSON file and writes the extracted data to it.

## Running the Script

```
python banks_append.py
```

## Output

The script will generate a JSON file named bank_data.json containing the extracted bank data.

## Example

For example, the input line:

```plaintext
Abhyudaya Co-op Bank    www.abhyudaya.com
will be converted to the following JSON entry:
```

```json
{
  "name": "Abhyudaya Co-op Bank",
  "url": "www.abhyudaya.com"
}
```

## Dependencies

1. Python 3.12
2. re (regular expression) module
3. json module

## License

This script is provided under the MIT License.
