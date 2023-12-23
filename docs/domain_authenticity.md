# Domain Registration Date Checker
This Python script utilizes the whois library to retrieve and display the registration date of a given domain. Additionally, it calculates and prints the time period since the domain was registered.

## Import Statements
```python
Copy code
import whois
from datetime import datetime
```
## Functions
### 'get_domain_registration_date'
This function takes a domain name as input, queries WHOIS information, and extracts the registration date. It then prints the registration date and calls the calculate_time_period function to determine the time period since registration.

```python

def get_domain_registration_date(domain_name):
    try:
        # Query WHOIS information
        domain_info = whois.whois(domain_name)

        # Extract registration date
        registration_dates = domain_info.creation_date
        if isinstance(registration_dates, list):
            registration_date = registration_dates[0]
        else:
            registration_date = registration_dates

        # Print the registration date
        print(
            f"The domain {domain_name} was registered on {registration_date}")

        # Compare with the current date and calculate the time period
        calculate_time_period(registration_date)

    except whois.parser.PywhoisError as e:
        print(f"Error: {e}")
```
### 'calculate_time_period'
This function calculates the time period between the registration date and the current date. It then prints the duration the domain has been registered.

```python

def calculate_time_period(registration_date):
    try:
        # Parse registration date and current date
        registration_date = datetime.strptime(
            str(registration_date), '%Y-%m-%d %H:%M:%S')
        current_date = datetime.now()

        # Calculate the time period
        time_period = current_date - registration_date

        # Print the time period
        print(f"The domain has been registered for {time_period.days} days.")

    except Exception as e:
        print(f"Error calculating time period: {e}")
```
## Example Usage
Replace the URL in the function call with the actual domain you want to check.

```python
# Replace 'https://shopifyplatform.shop/m/index' with the actual domain you want to check
get_domain_registration_date('https://shopifyplatform.shop/m/index')
```
## License
This project is licensed under the MIT License
