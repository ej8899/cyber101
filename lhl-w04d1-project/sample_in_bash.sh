#!/bin/bash

# chmod 755 sample_in_bash.sh
# this sets the permissions of the file to 755 (read, write, execute) 

# Pick a log file to search - comment the other one out.
LOG_FILE="apache_logs.txt"
# LOG_FILE="audit.log"

clear
echo "This is our apache_logs review program - running $(date)"

# not needed, but this gracefully exits if the log file does not exist.
if [ ! -f "$LOG_FILE" ]; then
    echo "The file $LOG_FILE does not exist."
    exit 1
fi

# just debugging - lets see what is in $LOG_FILE
echo "the log file is $LOG_FILE"


#
# uncomment any of the following code lines to see how things work
#

# egrep " 404 " "$LOG_FILE"

# egrep -e '([0-9]{3}\.)' "$LOG_FILE"

# IP searching in egrep - we'll find 183.*.*.* as an example:
# egrep -e '183\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}' "$LOG_FILE"


# the following two lines won't show on screen, 
# BUT will create a file in the current directory called temp_wp_admin_attempts.txt
# the output of the egrep command will be within the files.

# egrep "wp-admin" "$LOG_FILE" > temp_wp_admin_attempts.txt
# egrep "wp-admin" "$LOG_FILE"
# egrep " 404 " "$LOG_FILE" > temp_404_errors.txt

# egrep -e 'failed' "$LOG_FILE"


#
# IP address "pattern matching" using "sed" and "egrep" follows below:
#


# create a 'plain english' version of the IP pattern we want to search on.
# you can change this in any way.
# 150.*.*.* gives a few different IP results starting with 150
# 208.*.*.* gives a few differetn results too
# or you could do 208.115.*.* as another example
# you don't need to use an IP address here either.. 
# you can replace it with any plain text like we used in the examples above (like " 404 ",  or "wp-admin")

# comment or remove comments below to see how this works. 
# SEARCH_PATTERN="208.*.*.*"
# SEARCH_PATTERN="208.115.*.*"
# SEARCH_PATTERN=" 404 "
SEARCH_PATTERN="wp-admin"

# create a regex version of the IP pattern (if an IP pattern is detected)
# we use 'sed' which acts like a search and replace tool using regex patterns
# so we echo the IP pattern above into "sed" and tell it to replace the dots with backslashes OR (|) any 
# asterisks with [0-9]\{1,3\} - this is making a regex pattern out of the IP pattern we created above.
# it is saved in the variable REGEX_PATTERN
# sed is a command line tool, so we need to put it in quotes.
# sed works like this:
# 1. it searches the log file for the IP pattern
# 2. it replaces the dots with backslashes and a dot (remember our 'escape character') OR (|)
# 3. it replaces the asterisks with [0-9]\{1,3\}
REGEX_PATTERN=$(echo "$SEARCH_PATTERN" | sed 's/\./\\./g' | sed 's/\*/[0-9]\{1,3\}/g')
# show us the Regex pattern
echo "The regex pattern to search on is: $REGEX_PATTERN"
# search the log file for the Regex pattern and show results on screen.
# -o is an option that only shows the matching pattern, not the whole line.

# commands you can try below: 
# egrep -o "$REGEX_PATTERN" "$LOG_FILE"
# egrep without the -o shows us the full line
egrep -n "$REGEX_PATTERN" "$LOG_FILE"

# the following one creates the file temp_ip_search.txt and puts our output into it instead of the screen
#egrep "$REGEX_PATTERN" "$LOG_FILE" > temp_ip_search.txt