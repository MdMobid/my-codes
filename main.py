import telebot
from os import environ

BOT_TOKEN = environ.get('BOT_TOKEN', "")

# Creating Telebot Object
bot = telebot.TeleBot(BOT_TOKEN)

# Whenever Starting Bot
@bot.message_handler(commands=['start', 'hello'])
def send_welcome(message):

  markdown = f"""Hey *{message.chat.first_name}* Welcome To *My Telegram Bot*."""

  bot.reply_to(message, markdown, parse_mode="Markdown")
  print(f"Welcome Message Sent To {message.chat.first_name}\n")


# Handle Documents
@bot.message_handler(func=lambda m: True, content_types=['document'])
def handle_docs_photo(message):
  bot.reply_to(
      message,
      f"Sorry {message.chat.first_name}, Documents Not Supported At This Time")
  print(f"Message Replied To {message.chat.first_name}\n")


# Reply To All Messages
@bot.message_handler(func=lambda msg: True)
def all(message):
  bot.reply_to(
      message,
      f"Sorry {message.chat.first_name}, This Bot Is In Development Mode")
  print(f"Message Replied To {message.chat.first_name}\n")


print("Bot Started And Waiting For New Messages\n")

# Waiting For New Messages
bot.infinity_polling()