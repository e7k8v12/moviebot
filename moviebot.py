import telebot
from telebot import apihelper

# http://t.me/new_movie_list_bot
with open('token', 'r') as f:
    token = f.read() + " "
token = token.strip()

bot = telebot.TeleBot(token)


@bot.message_handler(commands=['start', 'go'])
def start_handler(message):
    bot.send_message(message.chat.id, 'Привет. Тут будет список новых фильмов.')


print("here")

bot.polling()
