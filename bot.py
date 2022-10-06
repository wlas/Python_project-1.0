import controller as con
import telebot
from telebot import types
import user_interface as ui
import print_db as pd
import search_db as sd
import export_db as ed
import import_db as id

bot = telebot.TeleBot('5655531070:AAHuI7gAGDelJnJc2EJWlXQ0uCaRiHVLzwo')
tel_data = ed.export_data()

@bot.message_handler(commands=['start'])
def start_message(message):
    bot.send_message(message.chat.id,'Телефонный справочник')

@bot.message_handler(commands=['button'])
def button_message(message):
    markup=types.ReplyKeyboardMarkup(resize_keyboard=True)
    item1=types.KeyboardButton("Вывести все контакты")
    item2=types.KeyboardButton("Добавить контакт")
    item3=types.KeyboardButton("Поиск контакта")
    markup.add(item1)
    markup.add(item2)
    markup.add(item3)
    bot.send_message(message.chat.id,'Выберите что вам надо',reply_markup=markup)


@bot.message_handler(content_types='text')
def message_reply(message):
    if message.text=="Вывести все контакты":        
        chat_id = message.chat.id
    bot.send_message(chat_id, '\n'.join(map(str, tel_data)))
    #elif message.text=="Добавить контакт":

bot.infinity_polling()    