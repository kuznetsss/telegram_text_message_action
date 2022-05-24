#!/usr/bin/env python3
import requests
import argparse
import json
import sys


def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument("-m", "--message", help="Message to send", required=True)
    parser.add_argument(
        "-c",
        "--chat-id",
        help="Chat id where to send the message",
        required=True,
    )
    parser.add_argument("-t", "--bot-token", help="Bot token", required=True)
    parser.add_argument(
        "-n",
        "--disable-notifications",
        help="Whether to disable notifications or not",
        type=bool,
    )
    parser.add_argument(
        "-p",
        "--disable-url-preview",
        help="Whether to disable url preview or not",
        type=bool,
    )
    return parser.parse_args()


def main():
    args = parse_args()

    data = {
        "chat_id": args.chat_id,
        # Telegram requires to escape dot symbol
        "text": args.message,
        "parse_mode": "Markdown",
        "disable_notifications": args.disable_notifications,
        "disable_web_page_preview": args.disable_url_preview,
    }
    reply = requests.post(
        url=f"https://api.telegram.org/bot{args.bot_token}/sendMessage", data=data
    )
    decoded_reply = json.loads(reply.content.decode("utf-8"))
    if decoded_reply["ok"]:
        exit(0)

    print(
        "Sending message failed with description:",
        decoded_reply["description"],
        file=sys.stderr,
    )
    exit(1)


if __name__ == "__main__":
    main()
