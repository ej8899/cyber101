import csv
import json
import requests
import time


# this code has been initally obtained from https://github.com/ph1nx/VirusTotal-Bulk-IP-Scanner
# and has been modified by erniejohnson.ca for the purposes of a specific project.


global apikey

apikey = ''  # Your VirusTotal API Key

# Function to check if an IP address is malicious
def check_ip(ip_address):
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
    
    print(f"IP: {ip_address}\tmalicious: {malicious}\tsuspicious {suspicious}")

    return {
        'IP Address': ip_address,
        'Country': country,
        'Owner': as_owner,
        'Malicious': malicious,
        'Suspicious': suspicious,
        'Undetected': undetected,
        'Total': total
    }

# Read the CSV file
input_file = 'IP_list.csv'  # Input CSV file path
output_file = 'IP_score.csv'  # Output CSV file path

try:
    with open(input_file, 'r', encoding='utf-8-sig') as infile:
        reader = csv.DictReader(infile)
        ip_list = list(reader)

    if len(ip_list) > 500:
        print("IP count exceeding VirusTotal rate limit. Checking malicious score for the first 500 IPs.")
        ip_list = ip_list[:500]

    with open(output_file, 'w', newline='', encoding='utf-8') as outfile:
        fieldnames = ['IP Address', 'Country', 'Owner', 'Malicious', 'Suspicious', 'Undetected', 'Total']
        writer = csv.DictWriter(outfile, fieldnames=fieldnames)

        writer.writeheader()
        for col in ip_list:
            try:
                column_name = 'IP_Address'  # Column name containing IP Addresses
                ip_address = col[column_name]
                # print(f"Started VirusTotal IP Scan...{ip_address}")
                data = check_ip(ip_address)
                writer.writerow(data)
                
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
    print("IP scan completed!!")

except FileNotFoundError:
    print("The specified file was not found.")
except Exception as e:
    print(f"An unexpected error occurred: {e}")