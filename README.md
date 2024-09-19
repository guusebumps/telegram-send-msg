# Telegram Bot Message Sender

This Python script sends a message to a specified Telegram chat using the Telegram Bot API. It reads the bot token and chat ID from configuration files and sends a predefined message.

## Features

- Reads Telegram bot token and chat ID from text files.
- Sends a test message to a specified Telegram chat.
- Handles errors and prints status messages to the console.

## Requirements

- `python-telegram-bot` library

## Installation

1. Clone the repository:
    ```bash
    git clone https://github.com/yourusername/telegram-bot-sender.git
    cd telegram-bot-sender
    ```

2. Install dependencies:
    ```bash
    pip install python-telegram-bot
    ```

## Configuration

You need to create two configuration files:

1. `telegram_token.txt`: This file should contain your Telegram bot token.
2. `telegram_chat_id.txt`: This file should contain the Telegram chat ID where the message will be sent.

Both files should be placed in the `configs/` directory.

## Contributing
    Make sure to replace `yourusername` with your actual GitHub username when uploading the file.
