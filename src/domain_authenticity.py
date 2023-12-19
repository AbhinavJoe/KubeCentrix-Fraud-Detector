import whois
from datetime import datetime


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


# Replace 'https://qubecentrix.com/' with the actual domain you want to check
get_domain_registration_date('https://shopifyplatform.shop/m/index')
