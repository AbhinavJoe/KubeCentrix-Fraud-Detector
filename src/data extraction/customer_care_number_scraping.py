import os
import requests
from bs4 import BeautifulSoup
import json


def extract_customer_care_number(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')

    # Modify this part based on the structure of the webpage to extract customer care numbers
    customer_care_numbers = [number.text for number in soup.find_all(
        "span", class_="customer-care")]

    return customer_care_numbers


def scrape_banks(banks):
    results = []

    for bank in banks:
        bank_name = bank["bank_name"]
        url = bank["url"]

        customer_care_numbers = extract_customer_care_number(url)

        results.append({
            "bank_name": bank_name,
            "customer_care_numbers": customer_care_numbers
        })

    return results


def main():
    # Load the input JSON file with bank details
    with open("banks_input.json", 'r') as json_file:
        banks_data = json.load(json_file)

    # Scrape the customer care numbers for each bank
    scraped_data = scrape_banks(banks_data)

    # Write the scraped data to the output JSON file
    with open("customer_care_numbers_output.json", 'w') as json_file:
        json.dump(scraped_data, json_file, indent=4)


if __name__ == "__main__":
    main()
