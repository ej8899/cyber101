#!/bin/bash

SOURCE_SERVER="webserver01"
DEST_SERVER="backupserver01"
MYSQL_USER="your_mysql_username"
MYSQL_PASSWORD="your_mysql_password"
DATABASE_NAME="your_database_name"
BACKUP_FILE="/tmp/${DATABASE_NAME}_backup.sql"

echo "Backing up database '${DATABASE_NAME}' on ${SOURCE_SERVER}..."
# export data to dump file
ssh ${SOURCE_SERVER} "mysqldump -u ${MYSQL_USER} -p${MYSQL_PASSWORD} ${DATABASE_NAME} > ${BACKUP_FILE}"

# error check
if [ $? -ne 0 ]; then
    echo "Error: Failed to backup database on ${SOURCE_SERVER}"
    exit 1
fi

echo "Copying backup file to ${DEST_SERVER}..."
# scp to copy across servers
scp ${SOURCE_SERVER}:${BACKUP_FILE} ${DEST_SERVER}:${BACKUP_FILE}

# error check
if [ $? -ne 0 ]; then
    echo "Error: Failed to copy backup file to ${DEST_SERVER}"
    exit 1
fi


echo "Cleaning up backup file on ${SOURCE_SERVER}..."
# remove dump file on source server
ssh ${SOURCE_SERVER} "rm -f ${BACKUP_FILE}"

# fin
echo "Database backup '${DATABASE_NAME}' successfully copied from ${SOURCE_SERVER} to ${DEST_SERVER}"