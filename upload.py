import os
import argparse
from pyrogram import Client

def upload_files_in_directory(directory, api_id, api_hash, bot_token):
    with Client("deltarvx", api_id=api_id, api_hash=api_hash, bot_token=bot_token) as app:
        chat_id = 'DeltaRevanced'  # Ganti dengan ID chat atau channel tujuan Anda

        for root, _, files in os.walk(directory):
            for filename in files:
                file_path = os.path.join(root, filename)
                
                # Menggunakan nama file sebagai caption saat mengunggahnya
                caption = f"File: {filename}"
                
                app.send_document(chat_id=chat_id, document=file_path, caption=caption)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Upload files in a directory to Telegram.')
    parser.add_argument('--dir', type=str, help='Directory path containing files to upload')
    parser.add_argument('--api_id', type=int, help='API ID for your Telegram app')
    parser.add_argument('--api_hash', type=str, help='API Hash for your Telegram app')
    parser.add_argument('--bot_token', type=str, help='Bot Token for your Telegram bot')

    args = parser.parse_args()

    if args.dir and args.api_id and args.api_hash and args.bot_token:
        directory = args.dir
        api_id = args.api_id
        api_hash = args.api_hash
        bot_token = args.bot_token

        upload_files_in_directory(directory, api_id, api_hash, bot_token)
    else:
        print("Please provide directory path, api_id, api_hash, and bot_token using appropriate arguments.")
