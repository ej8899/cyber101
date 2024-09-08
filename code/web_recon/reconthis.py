import requests
import urllib.parse

# ANSI color codes for colored output
RED = '\033[91m'
GREEN = '\033[92m'
BRIGHT = '\033[1m'
RESET = '\033[0m'

# List of words to append to the URL
word_list = ['example1', 'upload', 'uploads/', 'admin/', '2007/', 'lib/', 'login/']  # Add your list of words here

# Base domain URL (make sure to include the proper URL scheme, http or https)
base_url = 'https://www.erniejohnson.ca/'  # Try 'http://' as well if needed

# List to hold results
valid_urls = []
invalid_urls = []

# Set headers to mimic a browser
headers = {
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36',
    'Accept-Language': 'en-US,en;q=0.5',
}

# Function to check if a URL exists
def check_url(url):
    try:
        response = requests.get(url, headers=headers, allow_redirects=True)
        print(f"Checking {url} - Status Code: {response.status_code}")
        # Log response status code and check for 200
        if response.status_code == 200:
            return True
        else:
            return False
    except requests.RequestException as e:
        print(f"Error checking URL {url}: {e}")
        return False

# Loop through each word in the list
for word in word_list:
    # URL encode the word to handle special characters
    encoded_word = urllib.parse.quote(word)
    # Construct the full URL (with and without trailing slash)
    full_url = base_url + encoded_word + ''
    print(f"Checking URL: {full_url}")
    
    # Check if the URL exists
    if check_url(full_url):
        print(GREEN + f"URL exists: {full_url}" + RESET)
        valid_urls.append(full_url)
    else:
        print(RED + f"URL not found or 406 error: {full_url}" + RESET)
        invalid_urls.append(full_url)

# Print the results
print(BRIGHT + "\nValid URLs:" + RESET)
for url in valid_urls:
    print(GREEN + url + RESET)

print(BRIGHT + "\nInvalid URLs (404/406):" + RESET)
for url in invalid_urls:
    print(RED + url + RESET)
