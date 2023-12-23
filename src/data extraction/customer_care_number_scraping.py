import os
import requests
from bs4 import BeautifulSoup
import json

current_directory = os.path.dirname(os.path.realpath(__file__))
json_file_path = os.path.join(
    current_directory, "../../data/bank_data.json")


def extract_customer_care_number(url):
    try:
        # Adjust the timeout value as needed
        response = requests.get(url, timeout=10)
        response.raise_for_status()  # Raise an HTTPError for bad responses
    except requests.exceptions.RequestException as e:
        print(f"Error accessing {url}: {e}")
        return []

    soup = BeautifulSoup(response.content, 'html.parser')

    # Extract customer care numbers from <span> elements with class "customer-care"
    customer_care_numbers_span = [number.text.strip() for number in soup.find_all(
        "span", class_="customer-care")]

    # Extract customer care numbers from <a> elements with class "call-now-btn"
    customer_care_numbers_a = [a['title'] for a in soup.find_all(
        "a", class_="call-now-btn")]

    # Combine the extracted numbers from both <span> and <a> elements
    customer_care_numbers = customer_care_numbers_span + customer_care_numbers_a

    return customer_care_numbers


def scrape_banks(banks):
    results = []

    for bank in banks:
        bank_name = bank["name"]
        url = bank["url"]

        customer_care_numbers = extract_customer_care_number(url)

        results.append({
            "bank_name": bank_name,
            "customer_care_numbers": customer_care_numbers
        })

    return results


def main():
    # Load the input JSON file with bank details
    with open(json_file_path, 'r') as json_file:
        banks_data = json.load(json_file)

    # Scrape the customer care numbers for each bank
    scraped_data = scrape_banks(banks_data)

    # Write the scraped data to the output JSON file
    with open("customer_care_numbers_output.json", 'w') as json_file:
        json.dump(scraped_data, json_file, indent=4)


if __name__ == "__main__":
    main()
