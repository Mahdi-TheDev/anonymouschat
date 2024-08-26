import telebot
import base64


API_TOKEN = '7532549222:AAFFu9nMR7NHSJom-aU2QnT0WH8eSjmB8gA'

bot = telebot.TeleBot(API_TOKEN)

def encode_integer_to_string(number):
    number_bytes = number.to_bytes((number.bit_length() + 7) // 8, byteorder='big')
    encoded_string = base64.urlsafe_b64encode(number_bytes).decode('utf-8')
    return encoded_string

def decode_string_to_integer(encoded_string):
    number_bytes = base64.urlsafe_b64decode(encoded_string.encode('utf-8'))
    return int.from_bytes(number_bytes, byteorder='big')


def generate_start_link(token):
    bot_username = bot.get_me().username
    return f"https://t.me/{bot_username}?start={token}"


# Handle the /start command with a token
@bot.message_handler(commands=['start'])
def handle_start(message):
    # Extract the token from the /start command
    token = message.text.split(' ')[1] if len(message.text.split()) > 1 else None

    if token:
        # Handle the token (e.g., store it, validate it, etc.)
        target = decode_string_to_integer(token)
        bot.send_message(target, f"سلام")
    else:
        bot.reply_to(message, "ممنون از اینکه ربات استارت کردید برای دریافت لینک از /link استفاده کنید.")

@bot.message_handler(commands=['link'])
def link_gen(message):
    link = generate_start_link(encode_integer_to_string(message.chat.id))
    bot.reply_to(message,"سلام لینک شما :"+"\b"+f"{link}")
# Start polling (this keeps the bot running)
bot.polling()