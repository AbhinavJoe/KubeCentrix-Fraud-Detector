# Phishing Detection and SSL Verification API Documentation
## Introduction
This documentation provides details about two endpoints of the API: Phishing Detection and SSL Verification. These endpoints offer functionality to analyze a website for potential phishing content and check if it uses SSL encryption.

## Phishing Detection
## Endpoint: /scan (POST)
Request
Method: POST
Body:
url: The URL of the website to scan.
word_list: A list of words to check for on the website.
```json

{
  "url": "https://example.com",
  "word_list": ["login", "password", "phishing"]
}
```
## Response

## Success (200 OK):
matching_words: List of matching words found on the website.
count: Number of matching words.

```json

{
  "matching_words": ["login", "password"],
  "count": 2
}
Error (400 Bad Request):
Missing url or word_list.
json
Copy code
{
  "error": "Missing url or word_list"
}
Error (other):
Failed to retrieve the webpage.
json
Copy code
{
  "error": "Failed to retrieve the webpage"
}
```
SSL Verification
Endpoint: /check_ssl (POST)
Request
Method: POST
Body:
url: The URL of the website to check for SSL.
json
Copy code
{
  "url": "https://example.com"
}
Response
Success (200 OK):
url: The URL of the website.
ssl: Boolean indicating whether the website uses SSL.
message: Information about SSL usage.
json
Copy code
{
  "url": "https://example.com",
  "ssl": true,
  "message": "The website uses SSL."
}
Error (400 Bad Request):
Missing url.
json
Copy code
{
  "error": "Missing url"
}
Error (other):
Failed to retrieve the website or unexpected status code.
json
Copy code
{
  "url": "https://example.com",
  "error": "Failed to retrieve the website. Status code: 404"
}
