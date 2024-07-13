
# function to open logfile and give us it's contacts as a return variable
def parse_apache_log(logfile):
    with open(logfile, 'r') as file:
        log_entries = file.readlines()
    return log_entries

def find_errors(log_entries):
    failed_accesses = []
    not_found_errors = []
    for entry in log_entries:
        if ' 401 ' in entry or ' 403 ' in entry:
            failed_accesses.append(entry)
        if ' 404 ' in entry:
            not_found_errors.append(entry)
    return failed_accesses, not_found_errors

def find_suspect_ips(log_entries):
    ip_counts = {}
    for entry in log_entries:
        parts = entry.split()
        if len(parts) > 0:
            ip = parts[0]
            if ip in ip_counts:
                ip_counts[ip] += 1
            else:
                ip_counts[ip] = 1

    suspect_ips = {ip: count for ip, count in ip_counts.items() if count > 100}  # Adjust threshold as needed
    return suspect_ips

def display_results(failed_accesses, not_found_errors, suspect_ips):
    print("Failed Accesses (401 and 403):")
    for access in failed_accesses:
        print(access)
    print("\n404 Errors:")
    for error in not_found_errors:
        print(error)
    print("\nSuspect IP Addresses:")
    for ip, count in suspect_ips.items():
        print(f"{ip}: {count} requests")


#
# "main" part of program to run our functions from above
#

# set the logfile
logfile = 'apache_logs.txt'
log_entries = parse_apache_log(logfile)
failed_accesses, not_found_errors = find_errors(log_entries)
suspect_ips = find_suspect_ips(log_entries)

display_results(failed_accesses, not_found_errors, suspect_ips)
