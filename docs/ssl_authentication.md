# SSL Checker
This Python script checks if a given website uses SSL by sending an HTTP GET request and inspecting the URL.

## Import Statements
```python
import requests
```
## Function
### 'check_ssl'
This function takes a website URL as input, sends a GET request, and checks the response status. If the status code is 200, it then checks if the URL starts with "https://" to determine if SSL is used.

```python

def check_ssl(url):
    try:
        response = requests.get(url)
        if response.status_code == 200:
            if "https://" in response.url:
                print(f"The website {url} uses SSL.")
            else:
                print(f"The website {url} does not use SSL.")
        else:
            print(f"Failed to retrieve the website. Status code: {response.status_code}")
    except Exception as e:
        print(f"An error occurred: {e}")
```
## Example Usage
```python

# Example usage:
# Where the first and second websites do not have website authentication
# website_url = "http://www.china.com.cn/"
website_url = "http://chinanetrank.com/"
# website_url = "https://github.com/"
check_ssl(website_url)
```
## License
This script is provided under the MIT License.
