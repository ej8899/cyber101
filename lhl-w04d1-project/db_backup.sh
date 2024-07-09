#!/bin/bash

SOURCE_SERVER="linux-server"
DEST_SERVER="10.0.2.8"
MYSQL_USER="student"
MYSQL_PASSWORD="lighthouse"
DATABASE_NAME="prtg_test_db"
BACKUP_FILE="./${DATABASE_NAME}_backup.sql"

echo "Backing up database '${DATABASE_NAME}' from ${SOURCE_SERVER}..."

# export data to dump file
mysqldump -u ${MYSQL_USER} -p ${DATABASE_NAME} > ${BACKUP_FILE}

# error check
if [ $? -ne 0 ]; then
    echo "Error: Failed to backup database on ${SOURCE_SERVER}"
    exit 1
fi

echo "Copying backup file to ${DEST_SERVER}..."
# scp to copy across servers
scp ${BACKUP_FILE} student@${DEST_SERVER}:${BACKUP_FILE}

# error check
if [ $? -ne 0 ]; then
    echo "Error: Failed to copy backup file to ${DEST_SERVER}"
    exit 1
fi


echo "Cleaning up backup file on ${SOURCE_SERVER}..."
# remove dump file on source 
rm -f ${BACKUP_FILE}

# fin
echo "Database backup '${DATABASE_NAME}' successfully copied from ${SOURCE_SERVER} to ${DEST_SERVER}"
