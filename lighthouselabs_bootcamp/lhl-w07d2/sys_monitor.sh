#!/bin/bash

#
# lighthouse labs W07D2 - bash script for log monitoring
# Create a bash script that contains a set of Linux
# commands that perform any of these tasks.

# These tasks can range from:

# file management
# system monitoring
# network configuration
#

# Set the log file path
LOGFILE="./system_monitor.log"

# Function to log a message with a timestamp
log_message() {
    echo "$(date +'%Y-%m-%d %H:%M:%S') - $1" >> $LOGFILE
}

# Log the start of the monitoring
log_message "Starting system monitoring..."

# Check disk usage
log_message "Disk Usage:"
df -h >> $LOGFILE
log_message "-------------------------------------"

# Check memory usage
log_message "Memory Usage:"
free -h >> $LOGFILE
log_message "-------------------------------------"

# Check CPU load
log_message "CPU Load:"
uptime >> $LOGFILE
log_message "-------------------------------------"

# Check active network connections
log_message "Active Network Connections:"
netstat -tuln >> $LOGFILE
log_message "-------------------------------------"

# Log the end of the monitoring
log_message "System monitoring completed."

# Print the log file to the console (optional)
cat $LOGFILE
