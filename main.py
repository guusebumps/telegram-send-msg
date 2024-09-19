from telegram import Bot

def read_file_data(file_path):
    with open(file_path, 'r') as file:
        return file.read().strip()

telegram_token_path = './configs/telegram_token.txt'
telegram_chat_id_path = './configs/telegram_chat_id.txt'

telegram_token = read_file_data(telegram_token_path)
telegram_chat_id = read_file_data(telegram_chat_id_path)

def main():

    message = "Testing..."

    try:
        bot = Bot(token=telegram_token)
        bot.send_message(chat_id=telegram_chat_id, text=message)
        print("Message sent successfully!")
    except Exception as e:
        print(f"Error sending message: {e}")

if __name__ == "__main__":
    main()