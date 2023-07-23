#!/bin/bash

# Set the bot token and channel ID
TOKEN="YOUR_BOT_TOKEN"
CHANNEL_ID="YOUR_CHANNEL_ID"
PWD=$(pwd)

# Set the name of the folder to be zipped
folder="name"

# Set the date and time format
timestamp=$(date +"%H-%M_%d-%m-%Y")

# Set the path to the file that stores the counter value
counter_file="$PWD/backup_count.txt"

# Read the counter value from the file
if [ -f $counter_file ]; then
    counter=$(cat $counter_file)
else
    counter=0
fi

# Increment the counter value by 1
counter=$((counter + 1))

# Save the new counter value to the file
echo $counter > $counter_file

# Create the zip file name by adding the timestamp and counter
zipfile="${folder}_${timestamp}_${counter}.zip"

# Zip the folder with the specified zip file name
zip -r $zipfile $folder

# Set the text to be displayed as a caption
caption="File: $zipfile"

# Upload the zip file to the Telegram channel using a bot with a caption
curl -v -F "chat_id=$CHANNEL_ID" -F document=@$zipfile -F "caption=$caption" https://api.telegram.org/bot$TOKEN/sendDocument
