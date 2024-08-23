import csv
import json
import requests
import time
from datetime import datetime
import os
import ipaddress

#
# VirusTotal Automated Scanner
#
# v1.1 - 2024-08-22
#
# The current version of this code can be found at 
# https://github.com/ej8899/cyber101/blob/main/code/virustotal/
#


# Variables

# Your VirusTotal API Key:
apikey = ''

# Input CSV file path
input_file = 'ip_input.csv'
# the input file should be a csv file with a column named "Address"

# Output CSV file path
output_file = 'ip_score.csv'


#
# TODO list:
# - count IP's and estimate time to completion
# - add a progress bar
# - show duration of scan (in seconds/minutes/hours)
#


# Constants

RED = "\033[31m"
ORANGE = "\033[33m"
GREEN = "\033[32m"
BLUE = "\033[34m"
RESET = "\033[0m"



# Function to clear the screen
def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

# Function to pad the IP address to ensure alignment
def pad_ip(ip_address):
    max_length = 15  # Length of xxx.xxx.xxx.xxx
    return ip_address.ljust(max_length)

# Function to check if an IP address is local
def is_local_ip(ip_address):
    try:
        ip = ipaddress.ip_address(ip_address)
        return ip.is_private
    except ValueError:
        return False

# Initialize counters
local_ip_count = 0
other_ip_count = 0
malicious_ip_count = 0
suspicious_ip_count = 0

# Function to check if an IP address is malicious
def check_ip(ip_address):
    global local_ip_count, other_ip_count, malicious_ip_count, suspicious_ip_count
    
    if is_local_ip(ip_address):
        padded_ip = pad_ip(ip_address)
        print(f"{GREEN}IP: {padded_ip}\tLOCAL{RESET}")
        local_ip_count += 1
        return {
            'IP Address': padded_ip,
            'Country': 'LOCAL',
            'Owner': 'LOCAL',
            'Malicious': 0,
            'Suspicious': 0,
            'Undetected': 0,
            'Total': 0
        }

    url = f'https://www.virustotal.com/api/v3/ip_addresses/{ip_address}' 
    headers = {'x-apikey': apikey}
    response = requests.get(url, headers=headers)
    if response.status_code != 200:
        raise requests.exceptions.RequestException(f"API request failed with status code {response.status_code}")
    response_json = response.json()
    if 'data' not in response_json:
        raise ValueError("Invalid response structure")
    attributes = response_json['data']['attributes']
    
    # JSON response parameters
    as_owner = attributes.get('as_owner')
    country = attributes.get('country')
    stat_analysis = attributes.get('last_analysis_stats')
    
    malicious = stat_analysis.get('malicious')
    suspicious = stat_analysis.get('suspicious')
    undetected = stat_analysis.get('undetected')
    harmless = stat_analysis.get('harmless')
    
    total = int(malicious) + int(suspicious) + int(undetected) + int(harmless)
    other_ip_count += 1
    if malicious > 0:
        color = RED
        malicious_ip_count += 1
    elif suspicious > 0:
        color = ORANGE
        suspicious_ip_count += 1
    else:
        color = RESET

    padded_ip = pad_ip(ip_address)
    print(f"{color}IP: {padded_ip}\tmalicious: {malicious}\tsuspicious: {suspicious}{RESET}")

    return {
        'IP Address': padded_ip,
        'Country': country,
        'Owner': as_owner,
        'Malicious': malicious,
        'Suspicious': suspicious,
        'Undetected': undetected,
        'Total': total
    }

# Read the CSV file
try:
    clear_screen()

    start_time = datetime.now().strftime("%Y-%m-%d %H:%M")
    print(f"Start date of analysis: {start_time}\n")

    with open(input_file, 'r', encoding='utf-8-sig') as infile:
        reader = csv.DictReader(infile)
        ip_list = list(reader)

    if len(ip_list) > 500:
        print("IP count exceeding VirusTotal rate limit. Checking malicious score for the first 500 IPs.")
        # TODO filter out LOCAL ip's first
        ip_list = ip_list[:500]

    with open(output_file, 'w', newline='', encoding='utf-8') as outfile:
        fieldnames = ['IP Address', 'Country', 'Owner', 'Malicious', 'Suspicious', 'Undetected', 'Total']
        writer = csv.DictWriter(outfile, fieldnames=fieldnames)

        writer.writeheader()
        for col in ip_list:
            try:
                column_name = 'Address'  # Column name containing IP Addresses
                ip_address = col[column_name]
                data = check_ip(ip_address)
                writer.writerow(data)
                
                if not is_local_ip(ip_address):
                    time.sleep(15)  # Sleep to ensure we don't exceed 4 requests per minute (API rate limit)
                
            except KeyError:
                print(f"The CSV does not contain {column_name} header.")
                break
            except requests.exceptions.RequestException as e:
                print(f"An error occurred while checking IP {ip_address}: {e}")
                print("API rate limit per day might be completed.")
                break
            except Exception as e:
                print(f"An unexpected error occurred while processing IP {ip_address}: {e}")
                break
    
    end_time = datetime.now().strftime("%Y-%m-%d %H:%M")
    print(f"\nEnd date of analysis: {end_time}\n")

    # Display final counts
    print(f"{GREEN}LOCAL{RESET} IPs discovered: {local_ip_count}")
    print(f"{BLUE}OTHER{RESET} IPs discovered: {other_ip_count}")
    print(f"{RED}MALICIOUS{RESET} IPs discovered: {malicious_ip_count}")
    print(f"{ORANGE}SUSPICIOUS{RESET} IPs discovered: {suspicious_ip_count}")
    total_count = local_ip_count + other_ip_count
    print(f"\nIP scan completed... {ORANGE}{total_count}{RESET} IP's scanned.")

except FileNotFoundError:
    print("The specified file was not found.")
except Exception as e:
    print(f"An unexpected error occurred: {e}")
