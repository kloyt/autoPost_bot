# -*- coding: cp1251 -*-
import random

import os
import shutil

import telebot
import time

import config

CHANNEL_NAME = '@ComicsRUS'
TOKEN = config.TOKEN
TelegramBot = telebot.TeleBot(TOKEN)

second = 1000
minute = 60*second
hour = 60*minute

new_path = "new"
old_path = "old"


def avto_post(message):

        # зашли в папку new
        path = "files/" + CHANNEL_NAME + "/" + new_path
        files = os.listdir(path)

        # Получаем случайный каталог из папки (Название линейки комиксов (Например: Про дедпула))
        file = files[random.randint(0, len(files)-1)]
        TitleofComics = file

        # Путь к номерам комиксов (Получили список выпусков комиксов)
        path = path + "/" + file

        # Список комиксов
        files = os.listdir(path)

        photos = files[0]
        TitleofNUM = photos
        photos = os.listdir(path + "/" + photos)
        print(photos)

        TelegramBot.send_message(CHANNEL_NAME, text=TitleofComics + " ->")
        for photo in photos:

            if photo.split('.')[-1] == 'jpeg' or photo.split('.')[-1] == 'jpg':
                print("\n" + path + "/" + TitleofNUM + "/" + photo + " \n")
                photo = open((path + "/" + TitleofNUM + "/" + photo), "rb")
                # По идее на на этом этапе получаю список всех каталогов с комиксами (Получил)

                TelegramBot.send_photo(CHANNEL_NAME, photo=photo)
                photo.close()
                TelegramBot.send_photo(message.chat.id, "FILEID")

        TelegramBot.send_message(CHANNEL_NAME, text="<- " + TitleofComics)
        # print("переместить из "+path + "/" + TitleofNUM + " в "+"files/"+CHANNEL_NAME + "/" + old_path + "/" +
        # TitleofComics + "/")


        print(path)
        time.sleep(10000)
        shutil.move(r''+path, r'' + "files/"+CHANNEL_NAME + "/" + old_path + "/" + TitleofComics + "/")


# Если пользователь запрашивает /start ДОДЕЛАТЬ
@TelegramBot.message_handler(func=lambda message: True, content_types=["text"])
def command_start(message):
    print(message.text)
    avto_post(message)


if __name__ == '__main__':
    TelegramBot.polling(none_stop=True)
