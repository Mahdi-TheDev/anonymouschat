import telebot
import Encrypt


API_TOKEN = '7532549222:AAFFu9nMR7NHSJom-aU2QnT0WH8eSjmB8gA'

bot = telebot.TeleBot(API_TOKEN)



def generate_start_link(token):
    bot_username = bot.get_me().username
    return f"https://t.me/{bot_username}?start={token}"


@bot.message_handler(commands=['start'])
def handle_start(message):
    token = message.text.split(' ')[1] if len(message.text.split()) > 1 else None

    if token:
        target =Encrypt.decode_string_to_integer(token)
        bot.send_message(target, f"سلام")
    else:
        bot.reply_to(message, "ممنون از اینکه ربات استارت کردید برای دریافت لینک از /link استفاده کنید.")


@bot.message_handler(commands=['link'])
def link_gen(message):
    link = generate_start_link(Encrypt.encode_integer_to_string(message.chat.id))
    bot.reply_to(message,"سلام لینک شما :"+"\b"+f"{link}")
bot.polling()