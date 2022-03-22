import telebot
from telebot import types
import yaml
from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton

with open('config.yml') as f: 
    data = yaml.load(f, Loader=yaml.FullLoader)

bot = telebot.TeleBot(data["TOKEN"])

def gen_markup():
    markup = InlineKeyboardMarkup()
    markup.row_width = 2
    markup.add(InlineKeyboardButton("Yes", callback_data="cb_yes"),
                               InlineKeyboardButton("No", callback_data="cb_no"))
    return markup

@bot.callback_query_handler(func=lambda call: True)
def callback_query(call, message):
    if call.data == "cb_yes":
        bot.send_message(message.chat.id, "Огоо")
    elif call.data == "cb_no":
        bot.answer_callback_query(message.chat.id, "Не огооо")

@bot.message_handler(func=lambda message: True)
def message_handler(message):
    bot.send_message(message.chat.id, "What's next?", reply_markup=gen_markup())

bot.infinity_polling()


