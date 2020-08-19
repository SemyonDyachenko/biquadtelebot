import telebot
import requests
import random
import _config_
from telebot import apihelper
import unittest


telegram_bot = telebot.TeleBot(_config_.telegram_token)

#receive messages from website chat
def on_receiving(chat_id):
    pass


@telegram_bot.message_handler(commands=['start'])
def _bot_start(message):
    if message.chat.type == "group":
        admins = apihelper.get_chat_administrators(_config_.telegram_token,message.chat.id)
        for user in admins:
            if user['user']['id'] == apihelper.get_me(_config_.telegram_token)['id']:
                telegram_bot.send_message(message.chat.id,"Set unique id with /setid")
                break
            else:
                telegram_bot.send_message(message.chat.id,"Please promote me to admin")    
    else:
        telegram_bot.send_message(message.chat.id,"Please add me to group")

@telegram_bot.message_handler(commands=['setid'])
def _set_id(message):
    pass
    

#check for non-existent commands
@telegram_bot.message_handler(content_types=['text'])
def _message_handle(message):
    if message.text[0] == "/": #first symbol
        if message.text != "/start":
            telegram_bot.send_message(message.chat.id,"Warning ! Bot understood only commands")


telegram_bot.polling(none_stop = True)