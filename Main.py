# -*- coding: cp1251 -*-
import os

import telebot
import time

CHANNEL_NAME = '@ComicsRUS'
TOKEN = ""
TelegramBot = telebot.TeleBot(TOKEN)

second = 1000
minute = 60*second
hour = 60*minute

new_path = "files/new/"
old_path = "files/old/"


def avto_post(message):
    while True:
        for file in os.listdir(new_path):
            print(file)
            if file.split('.')[-1] == 'jpeg' or file.split('.')[-1] == 'jpg':
                file = open((new_path + file), "rb")
                TelegramBot.send_photo(CHANNEL_NAME, photo=file)
                file.close()
                #   TelegramBot.send_photo(message.chat.id, "FILEID")
                time.sleep(second*10)


# Если пользователь запрашивает /start ДОДЕЛАТЬ
@TelegramBot.message_handler(func=lambda message: True, content_types=["text"])
def command_start(message):
        avto_post(message)
        print(message.text)

if __name__ == '__main__':
    TelegramBot.polling(none_stop=True)
