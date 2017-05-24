# -*- coding: cp1251 -*-
import random

import os
import shutil

import telebot

import config

CHANNEL_NAME = '@ComicsRUS'
TOKEN = config.TOKEN
TelegramBot = telebot.TeleBot(TOKEN)

second = 1000
minute = 60 * second
hour = 60 * minute

new_path = "new"
old_path = "old"


def autorization(name):
    if config.adminList.count(name) > 0: return True
    else: return False


def avto_post(message):
    # ����� � ����� new
    path = "files/" + CHANNEL_NAME + "/" + new_path
    files = os.listdir(path)

    # �������� ��������� ������� �� ����� (�������� ������� �������� (��������: ��� �������))
    file = files[random.randint(0, len(files) - 1)]
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
            # print("\n" + path + "/" + TitleofNUM + "/" + photo + " \n")
            photo = open((path + "/" + TitleofNUM + "/" + photo), "rb")
            # �� ���� �� �� ���� ����� ������� ������ ���� ��������� � ��������� (�������)

            TelegramBot.send_photo(CHANNEL_NAME, photo=photo)
            photo.close()
    TelegramBot.send_message(CHANNEL_NAME, text="<- " + TitleofComics)
    # print("����������� �� "+path + "/" + TitleofNUM + " � "+"files/"+CHANNEL_NAME + "/" + old_path + "/" +
    # TitleofComics + "/")

    shutil.move(r'' + path + "/" + TitleofNUM,
                r'' + "files/" + CHANNEL_NAME + "/" + old_path + "/" + TitleofComics + "/")


@TelegramBot.message_handler(func=lambda message: True, content_types=["text"])
def command_start(message):
    print(message.chat.username)
    if autorization(message.chat.username):
        avto_post(message)
    else:
        TelegramBot.send_message(message.chat.id, text="����� �������������� ����� ���� �� ������ ����� ��� "
                                                       "���������������")

if __name__ == '__main__':
    TelegramBot.polling(none_stop=True)
