# Zip and Upload Script

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

## Setting up a Cron Job

You can set up a cron job to run this shell script automatically at specified times. Here's how:

1. Open your crontab file by running `crontab -e`.
2. Add a new line to schedule when you want to run this script. For example, if you want to run it every day at 5 AM and 5 PM, you can add this line:
3. 0 5,17 * * * /path/to/script.sh

Make sure to replace `/path/to/script.sh` with the actual path to your shell script.
3. Save your changes and close your crontab file.

The cron job will now run this shell script automatically at the specified times.

