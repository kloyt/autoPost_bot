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

        # ����� � ����� new
        path = "files/" + CHANNEL_NAME + "/" + new_path
        files = os.listdir(path)

        # �������� ��������� ������� �� ����� (�������� ������� �������� (��������: ��� �������))
        file = files[random.randint(0, len(files)-1)]
        TitleofComics = file

        # ���� � ������� �������� (�������� ������ �������� ��������)
        path = path + "/" + file

        # ������ ��������
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
                # �� ���� �� �� ���� ����� ������� ������ ���� ��������� � ��������� (�������)

                TelegramBot.send_photo(CHANNEL_NAME, photo=photo)
                photo.close()
                TelegramBot.send_photo(message.chat.id, "FILEID")

        TelegramBot.send_message(CHANNEL_NAME, text="<- " + TitleofComics)
        # print("����������� �� "+path + "/" + TitleofNUM + " � "+"files/"+CHANNEL_NAME + "/" + old_path + "/" +
        # TitleofComics + "/")


        print(path)
        time.sleep(10000)
        shutil.move(r''+path, r'' + "files/"+CHANNEL_NAME + "/" + old_path + "/" + TitleofComics + "/")


# ���� ������������ ����������� /start ��������
@TelegramBot.message_handler(func=lambda message: True, content_types=["text"])
def command_start(message):
    print(message.text)
    avto_post(message)


if __name__ == '__main__':
    TelegramBot.polling(none_stop=True)
