# The Python code scans a given website for potential phishing by checking the legitimacy by following the given wordlist.

import requests
from bs4 import BeautifulSoup
import re

def Website_scanning (url, word_list):
    
    # Make a request to the website

    response = requests.get(url)

    # Check if the request was successful (status code 200)
    if response.status_code == 200:
        # Parse the HTML content of the page
        soup = BeautifulSoup(response.text, 'html.parser')

        # Extract text content from all elements
        all_text = ' '.join([element.get_text(separator=' ') for element in soup.find_all(['p', 'h1', 'h2', 'h3', 'h4', 'h5', 'h6', 'span', 'div'])])

        # Find all the words that match the ones in the provided list
        matching_words = [word for word in re.findall(r'\b\w+\b', all_text) if word.lower() in map(str.lower, word_list)]

        # Print the matching words and their count
        print("Matching words found:", matching_words)
        print("Number of matching words:", len(matching_words))
    else:
        print("Failed to retrieve the webpage. Status code:", response.status_code)

# Example usage
url_input = input("Enter the website link to scan: ")

#  test site : https://fitgirl-repacks.site/all-switch-emulated-repacks-a-z/

# this wordlist is just for an sample list to test the code 

word_list = ['repacks' , 'game']



Website_scanning(url_input, word_list)
