import json, argparse, os
from datetime import datetime, timedelta

os.system('clear')

RED   = "\033[1;31m"  
BLUE  = "\033[1;34m"
CYAN  = "\033[1;36m"
GREEN = "\033[0;32m"
YELLOW = "\033[1;33m"
RESET = "\033[0;0m"

def read_log(file_path):
    with open(file_path, 'r') as file:
        log_entries = json.load(file)
    return log_entries

log_file_path = 'samplelogdata.json'
log_entries = read_log(log_file_path)

def filter_failed_logins(log_entries,days):
    now = datetime.now()
    time_span = now - timedelta(days=days)

    # Filter failed logins for x days
    filtered_entries = [
        entry for entry in log_entries
        if entry['status'].lower() == 'failed' and time_span <= datetime.fromisoformat(entry['timestamp']) <= now
    ]

    # Sort uid & timestamp in desc. order
    sorted_entries = sorted(
        filtered_entries,
        key=lambda x: (datetime.fromisoformat(x['timestamp']), x['user_id']),
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
  
    current_date = None

    #for entry in failed_logins:
    for i in range(len(failed_logins)):
        out_of_range_flag = False
        warning_message_flag = False
        entry = failed_logins[i]
        timestamp = datetime.fromisoformat(entry['timestamp'])
        entry_date = timestamp.date()
        user_id = entry['user_id']
        warning_message = ""
        if i > 0:
              prev_entry = failed_logins[i - 1]
              prev_timestamp = datetime.fromisoformat(prev_entry['timestamp'])
              prev_user_id = prev_entry['user_id']
              if user_id == prev_user_id and (prev_timestamp - timestamp).total_seconds() <= 5:
                  warning_message = f"{YELLOW}Warning: Multiple login attempts within 5 seconds{RESET}"
                  warning_message_flag = True
        
        ip_address = entry['ip_address']
        first_octet = int(ip_address.split('.')[0])
        if first_octet != 192:
            out_of_range = f"{RED}CAUTION: foreign IP{RESET}"
            out_of_range_flag = True
        else:
            out_of_range = f"{GREEN}{RESET}"

        # future use:
        # user_agent = entry['user_agent']
        # error_message = entry['error_message']
        if entry_date != current_date:
            current_date = entry_date
            print(f"\n{GREEN}{current_date}{RESET}")
            print(f"{BLUE}-" * 10)

        warning_messages = ""
        if args.thoughts and (out_of_range_flag or warning_message_flag):
            warning_messages = f" - {out_of_range} {warning_message}"

        print(f"{RESET}User ID: {CYAN}{user_id}{RESET}, Timestamp: {GREEN}{timestamp}{RESET}, IP Address: {GREEN}{ip_address}{RESET}{warning_messages}")
        

#
# Main
#
parser = argparse.ArgumentParser(description="Show failed logins from our log file and optionally provide security concerns.")
parser.add_argument('-e', '--email', action='store_true', help="Output in plain text format")
parser.add_argument('-t', '--thoughts', action='store_true', help="Add security concerns to report")
parser.add_argument('-d', '--days', type=int, default=7, help="Report for past x days (default 7 days)")

args = parser.parse_args()
num_days_to_report=args.days; 
failed_logins = filter_failed_logins(log_entries, num_days_to_report)

if args.email:
    RED   = ""  
    BLUE  = ""
    CYAN  = ""
    YELLOW = ""
    GREEN = ""
    RESET = ""
    
show_summary(failed_logins, num_days_to_report)