import os
import argparse
import json
from pyrogram import Client

def load_config(config_file):
    with open(config_file, 'r') as f:
        config = json.load(f)
    return config

def upload_file(api_id, api_hash, bot_token, chat_id, file_path):
    with Client("deltarvx", api_id=api_id, api_hash=api_hash, bot_token=bot_token) as app:
        # Menggunakan nama file sebagai caption saat mengunggahnya
        caption = f"File: {os.path.basename(file_path)}"
        app.send_document(chat_id=chat_id, document=file_path, caption=caption)

def upload_files_in_directory(directory, api_id, api_hash, bot_token, chat_id):
    for root, _, files in os.walk(directory):
        for filename in files:
            file_path = os.path.join(root, filename)
            upload_file(api_id, api_hash, bot_token, chat_id, file_path)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Upload files in a directory or specific file to Telegram.')
    parser.add_argument('--config', type=str, help='Path to the configuration file')
    parser.add_argument('--dir', type=str, help='Directory path containing files to upload')
    parser.add_argument('--file', type=str, help='Specific file path to upload')
    parser.add_argument('--api_id', type=int, help='API ID for your Telegram app')
    parser.add_argument('--api_hash', type=str, help='API Hash for your Telegram app')
    parser.add_argument('--bot_token', type=str, help='Bot Token for your Telegram bot')
    parser.add_argument('--chat_id', type=str, help='ID chat or channel for uploading')

    args = parser.parse_args()

    if args.config:
        config_file = args.config
        if os.path.exists(config_file):
            config = load_config(config_file)

            api_id = config.get('api_id', args.api_id)
            api_hash = config.get('api_hash', args.api_hash)
            bot_token = config.get('bot_token', args.bot_token)
            chat_id = config.get('chat_id', args.chat_id)
            file_path = config.get('file_path', args.file)
            directory = config.get('directory', args.dir)

            if file_path:
                upload_file(api_id, api_hash, bot_token, chat_id, file_path)
            elif directory:
                upload_files_in_directory(directory, api_id, api_hash, bot_token, chat_id)
            else:
                print("Please provide either 'file_path' or 'directory' in the configuration.")
        else:
            print("Config file not found.")
    elif args.api_id and args.api_hash and args.bot_token and args.chat_id:
        api_id = args.api_id
        api_hash = args.api_hash
        bot_token = args.bot_token
        chat_id = args.chat_id

        if args.file:
            upload_file(api_id, api_hash, bot_token, chat_id, args.file)
        elif args.dir:
            upload_files_in_directory(args.dir, api_id, api_hash, bot_token, chat_id)
        else:
            print("Please provide either --file or --dir argument.")
    else:
        print("Please provide api_id, api_hash, bot_token, and chat_id using appropriate arguments.")
          
