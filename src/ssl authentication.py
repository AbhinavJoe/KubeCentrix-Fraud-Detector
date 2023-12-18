# Importing requests module which allows you to send HTTP request
import requests


#Creating a function to check SSL 
def check_ssl(url): 
    
# Try block: Attempt to send a GET request to the specified URL, check the response status

    try:  
        response = requests.get(url)  
        if response.status_code == 200:   

           # Check if the URL starts with "https://" indicating SSL usage.
            
            if "https://" in response.url:
                print(f"The website {url} uses SSL.")

            else:
                print(f"The website {url} does not use SSL.")
        else:
            print(f"Failed to retrieve the website. Status code: {response.status_code}")
    except Exception as e:
        print(f"An error occurred: {e}")

# Example usage:
# Where the first and second website doesnot have the website authentication 
# website_url = "http://www.china.com.cn/"    
website_url = "http://chinanetrank.com/" 
# website_url = "https://github.com/"
check_ssl(website_url)
