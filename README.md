# Zip and Upload Script to Telegram Chat

This shell script zips a specified folder, adds a timestamp and counter to the zip file name, then uploads the zip file to a Telegram channel using a bot.

## Usage

1. Open the script with a text editor and set the `TOKEN` and `CHANNEL_ID` variables to your bot token and Telegram channel ID.
2. Set the `folder` variable to the name of the folder you want to zip.
3. Save the changes and close the file.
4. Give the script execute permission by running `chmod +x /path/to/script.sh`, where `/path/to/script.sh` is the path to your shell script.
5. Run the script by executing `/path/to/script.sh`. The script will zip the specified folder, add a timestamp and counter to the zip file name, then upload the zip file to the specified Telegram channel using a bot.

## Customization

You can customize the behavior of the script by changing the values of the variables at the top of the script:

- `TOKEN`: The bot token to be used for uploading the zip file to Telegram.
- `CHANNEL_ID`: The ID of the Telegram channel where the zip file will be uploaded.
- `folder`: The name of the folder to be zipped.
- `timestamp`: The date and time format to be added to the zip file name.
- `counter_file`: The path to the file that stores the counter value.

