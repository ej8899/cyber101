import json
import os
from datetime import datetime

def append_to_log(user_id, status, ip_address, user_agent, error_message):
    log_file = 'logins.json';
    log_entry = {
        "timestamp": datetime.now().isoformat(),
        "user_id": user_id,
        "status": status,
        "ip_address": ip_address,
        "user_agent": user_agent,
        "error_message": error_message
    }

    # Check if the log file exists
    if not os.path.exists(log_file):
        with open(log_file, 'w') as file:
            json.dump([], file)

    # Read the existing log entries and append the new entry
    with open(log_file, 'r') as file:
        log_entries = json.load(file)

    log_entries.append(log_entry)

    # Write the updated log entries back to the file
    with open(log_file, 'w') as file:
        json.dump(log_entries, file, indent=4)

# Example usage:
append_to_log(user_id="user123", status="failed", ip_address="192.168.1.17", user_agent="Mozilla/5.0", error_message="Invalid password")