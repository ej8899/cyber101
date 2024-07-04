import requests
import time

# HIBP API v3 docs: https://haveibeenpwned.com/API/v3
# HIBP - purchase an API key: https://haveibeenpwned.com/API/Key

def check_email(email, api_key):
    url = f"https://haveibeenpwned.com/api/v3/breachedaccount/{email}"
    headers = {
        'hibp-api-key': api_key,
        'User-Agent': 'HIBP API Python Client'
    }
    response = requests.get(url, headers=headers)
    
    if response.status_code == 200:
        return response.json()  # Returns the list of breaches
    elif response.status_code == 404:
        return []  # No breaches found
    else:
        response.raise_for_status()

# email addresses to check
email_list = ["email1@example.com", "email2@example.com", "email3@example.com"]

# HIBP API key
api_key = 'your_api_key_here'

# Check each email address
for email in email_list:
    try:
        breaches = check_email(email, api_key)
        if breaches:
            print(f"{email} has been found in the following breaches:")
            for breach in breaches:
                print(f" - {breach['Name']}")
        else:
            print(f"{email} has not been found in any breaches.")
        
        # Be mindful of rate limits
        time.sleep(1.5)  # Adjust sleep time according to HIBP rate limits
        
    except requests.exceptions.HTTPError as err:
        print(f"Error checking {email}: {err}")

