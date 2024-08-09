#!/bin/bash

clear
echo "Copying Log file to current directory..."
source_filename="../apache_logs.txt"


# check to see if the source filename (including the path) exists:
if [ ! -f "$source_filename" ]; then
  echo "Error: Our source file $source_filename does not exist."
  exit 1
fi


# below copies with fixed filename for the output
# cp /var/log/apache2/apache-logs.txt ./apache_logs_copy.txt

current_date=$(date +"%Y%m%d")

# Construct the new filename with the date appended
new_filename="apache_logs_copy_${current_date}.txt"
echo "New filename is $new_filename"

# the -e lets us use escape characters (the \  - and here the \n is for newline)
echo -e "\n"

# Copy the log file to the current directory with the new filename
cp "$source_filename" "./$new_filename"

# below the $? checks the return code of the last command (cp - for copy)
if [ $? -eq 0 ]; then
  echo -e "\nDone copying to $new_filename"
else
  echo "ERROR: Failed to copy to $new_filename."
  exit 1
fi