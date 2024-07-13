
# function to open logfile and return its contents
def parse_apache_log(logfile):
    with open(logfile, 'r') as file:
        log_entries = file.readlines()
    return log_entries

# function to read log entries and create list of failed_accesses and not_found_errors
def find_errors(log_entries):
    # create blank lists to hold entries with errors
    failed_accesses = []
    not_found_errors = []

    # loop thru each line in our log file:
    for entry in log_entries:
        # we need to search for the error codes with spaces around them to separate them from valid data that could be in time codes, or other information.
        if ' 401 ' in entry or ' 403 ' in entry:
            # add log item to list of failed_accesses
            failed_accesses.append(entry)
        if ' 404 ' in entry:
            # add log item to list of not_found_errors
            not_found_errors.append(entry)
    return failed_accesses, not_found_errors


# function to display our access errors
def display_results(failed_accesses, not_found_errors):
    # handle 401 and 403 errors here
    # 401 and 403 deal with authorization problems with the server to user (IoC)
    print("Failed Authorization Accesses (both 401 and 403):")
    for access in failed_accesses:
        print(access)
    # handle 404 errors here:
    # 404 errors can indicate potential 'probing' of a web server to find admin files with insecure passwords in them.
    # they are not always a concern, but need to be reviewed to create awareness of a possible attacker performing recon on the web server
    print("\n404 Errors:")
    # loop throug the list of not found errors and print each one to the screen.
    for error in not_found_errors:
        print(error)
    


#
# "main" part of program that runs our functions from above:

# set the logfile and location
logfile = 'apache_logs.txt'

# read the log file and save it to variable log_entries
log_entries = parse_apache_log(logfile)

# run the find_errors function with the log_entries data.
# it will return both failed access and not found errors into two variables:
failed_accesses, not_found_errors = find_errors(log_entries)

# run function to show us the errors
display_results(failed_accesses, not_found_errors)
