import json, argparse, os
from datetime import datetime, timedelta

RED   = "\033[1;31m"  
BLUE  = "\033[1;34m"
CYAN  = "\033[1;36m"
GREEN = "\033[0;32m"
RESET = "\033[0;0m"

def read_log(file_path):
    with open(file_path, 'r') as file:
        log_entries = json.load(file)
    return log_entries

log_file_path = 'samplelogdata.json'
log_entries = read_log(log_file_path)

def filter_failed_logins(log_entries,days):
    now = datetime.now()
    one_week_ago = now - timedelta(days)

    # Filter failed logins for x days
    filtered_entries = [
        entry for entry in log_entries
        if entry['status'] == 'failed' and one_week_ago <= datetime.fromisoformat(entry['timestamp']) <= now
    ]

    # Sort uid & timestamp in desc. order
    sorted_entries = sorted(
        filtered_entries,
        key=lambda x: (x['user_id'], datetime.fromisoformat(x['timestamp'])),
        reverse=True
    )
    return sorted_entries

def show_summary(failed_logins,days, plain_text=False):
    now = datetime.now()
    formatted_date_time = now.strftime("%A, %B %d, %Y %I:%M %p")
    count = len(failed_logins)
  
    print(f"{GREEN}Turn a New Leaf Youth Employment Agency{RESET}")
    print(f"Report as of {BLUE}{formatted_date_time}{RESET}\n")
    print(f"{BLUE}Summary of {RED}({count}) Failed{BLUE} Logins (Last {RED}{days}{BLUE} Days):{RESET}")
  
    for entry in failed_logins:
        timestamp = entry['timestamp']
        user_id = entry['user_id']
        ip_address = entry['ip_address']
        user_agent = entry['user_agent']
        error_message = entry['error_message']
        print(f"User ID: {CYAN}{user_id}{RESET}, Timestamp: {GREEN}{timestamp}{RESET}, IP Address: {GREEN}{ip_address}{RESET}, User Agent: {GREEN}{user_agent}{RESET}")

parser = argparse.ArgumentParser(description="Show failed logins")
parser.add_argument('-e', '--email', action='store_true', help="Output in plain text format")
parser.add_argument('-d', '--days', type=int, default=7, help="Report for past x days (default 7 days)")

args = parser.parse_args()
num_days_to_report=args.days; 
failed_logins = filter_failed_logins(log_entries, num_days_to_report)

if args.email:
    RED   = ""  
    BLUE  = ""
    CYAN  = ""
    GREEN = ""
    RESET = ""
    
show_summary(failed_logins, num_days_to_report)