# -*- coding: cp1251 -*-
import time

import telebot
from telebot import types

bot = telebot.TeleBot('5943394315:AAEHraI-8AwFmhAfH-GL0yfNu-3_3SWuPsk')

@bot.message_handler(commands=['start'])
def start(message):
    try:
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton('1')
        btn2 = types.KeyboardButton('2')
        btn3 = types.KeyboardButton('3')
        markup.add(btn1, btn2, btn3)
        helo = f'������c����, <b>{message.from_user.first_name}</b>! ��� ��� ����������? ��������: \n1 - ���� �� ������ ������ � ����� ����� \n2 - ���� �� ������ ������ ��� ���e ����������\n3 - ���� � ��� ��������� ��������'
        bot.send_message(message.chat.id, helo, parse_mode='html', reply_markup=markup)
        bot.register_next_step_handler(message, select)
    except:
        bot.send_message(message.chat.id, '<b>�� �����!</b>', parse_mode='html')

def select(message):
    try:
        if (message.text == '1'):
            aboutus(message)
        elif (message.text == '3'):
            learning(message)
        elif (message.text == '2'):
            productcs(message)
    except:
        bot.send_message(message.chat.id, '<b>�� �����!</b>', parse_mode='html')

@bot.message_handler(commands=['about'])
def aboutus(message):
    try:
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton('����� �����')
        btn2 = types.KeyboardButton('���-������')
        markup.add(btn1, btn2)
        bot.send_message(message.chat.id, '��� �� ������ ������ � �����?', reply_markup=markup)
        bot.register_next_step_handler(message, office)

    except:
        bot.send_message(message.chat.id, '<b>�� �����!</b>', parse_mode='html')

def office(message):
    try:
        if (message.text == '����� �����'):
            bot.send_photo(message.chat.id, 'https://cdn.discordapp.com/attachments/1093571641088413706/1095608257395032157/image.png')
            time.sleep(2)
            start(message)
        elif (message.text == '���-������'):
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            emp1 = types.KeyboardButton('������')
            emp2 = types.KeyboardButton('��������')
            emp3 = types.KeyboardButton('��������')
            emp4 = types.KeyboardButton('��������-��������')
            markup.add(emp1, emp2, emp3, emp4)
            bot.send_message(message.chat.id, '� ���������� ������ ���� ���������� �� ������ ������?', reply_markup=markup)
            bot.register_next_step_handler(message, staff)
    except:
        bot.send_message(message.chat.id, '<b>�� �����!</b>', parse_mode='html')

def staff(message):
    try:
        if (message.text == '��������'):
            bot.send_message(message.chat.id,
                             '������� ���� �������� - ������� frontend �����������, ������� �������� � ����� IT ��� 11 ���. �� ���������������� �� frontend ����������, � ������� �� �������� ��������� �����, ������ � ��������. ��� ������ � ���� � ���� ������� �������� ��������� ��������� ������ � ��� �������. ������� ���� �������� �������� ��������� �������� ������ ����������������, ����� ��� Python, C++, Kotlin. �� ����� ����� ������� ���� � ��������� ����������� � ����������� ��� frontend ����������. �� ����� ������ �������������� � ����� ����������� � ������������, ��� ��������� ��� ��������� ������������������ � ������������� �������. ����� ����, ������� ���� �������� �������� ��������� � ������� � ���������������� �����. �� ������� ������ �������� ������� � ������� �����������, ��� �������� ��������� ������ ���������������� ����������. ������� ���� �������� �������� ������ ������� �������������, � ��� ���������������� ������ � ������ �������� � ���������� �������� ��������� ��� ��������� ���������� ��������. �� ����� ����� �������� ������ �������� � ������ � ������� ������� �������, ����� ���������� ������ ��������� ��� �������. � �����, ������� ���� �������� - ��� ������� � ����������� frontend �����������, ������� �������� ����� ������������ �������� � �������� ��� �������� ������������������, ����������� � ������������� frontend ������� ��� ����� �������� � �������.')
            time.sleep(2)
            start(message)
        elif (message.text == '��������-��������'):
            bot.send_message(message.chat.id,
                             '������� ������� ���������� - ������� project ��������, ������� �������� � ����� ������������ ��� 13 ���. �� ���������������� �� ������ � ������ � ����� �������� ��������� ��������, ������� �������� ��� ���������� ��������� ��������� � ��������� ������������ �����. ������� ������� ���������� ����� �������� ��������� �������� � ������� ����������������, ��� ��������� ��� ����� �������� ������ ������� � ��������� ����� ����������� �������������� �������. �� ����� ����������� � ��������������, ����� ��������, ����� ���������� ������������ � ����� ������� ����� ����� �������� ��� ����������� �������. ������, �������� ����� �������� ������� ����������� - ��� ��� ����������� �������� � ������. �� ������ ����������� � ����������, ��� �������� ��� �������� ����������� � ��������� ������� ����� �������. �� ����� �������� ����� ���� � ������ � ������� ����������� ���������������� ���������, ��� ��������� ��� ����������� ��������� ���� � ������ �������. ������� ������� ���������� ����� ���� ������ �� ��������� �������� � � ��������� ����������, ��� ��������� ��� ��������� ������� ������� � ���������� ��������� �������. �� ������� ������ �������� �������� �� �������� � �������, ����� ������ ��� �������� ������� � � ������ �������. � �����, ������� ������� ���������� - ��� ������� � ����������� project ��������, ������� �������� ����� ������������ �������� � �������� ��� ������������ ���������� ���������. ��� ���������������� � ��������� �������� ��������� ��� ���������� �������� � �������� � ��������� ������������ �����.')
            time.sleep(2)
            start(message)
        elif (message.text == '��������'):
            bot.send_message(message.chat.id,
                             '����� ������� ������������� - ��������� �������� � ����� ������������ �������, ������� ��� ����� 15 ��� �������� � ���� �������. ��� ���������� ����� � ��������������� ������� ��� ����� �� ����� �������������� ���������� � ������. ����� ������� ���������������� �� �������� ������� ������, ���-����� ������ � ������ ��������, ��������� � ����������� ��������. �� ��������� ������� ������������ � �������� ��������� ����������, ������� ������������ � ����������� �������. ��� ������ ���������� ������� ��������� � �������������� ���������, ������� �������� �������� ������� �� ������-�����. ����� ������� ����� �������� ����� ������������ ������� ������� � �������� �� �����������, ����� ��������� ������, ������� ��������� ������� �������� �� �����������. �� ��������� ����������� ��������� ��������� � ����� ���������� � ���������, ����� ������������ ����� �������� ������ ���������� ��������� � ����������� �������. ����� ����, ����� ������� �������� �������� ���������� ���������� ����������, ��������� � ������ ������������ � ������������ �� �������, ��� �������� ��� ���� � ����� ��������� ��������� � ������ �������. � �����, ����� ������� ������������� - ��� ������� � ����������� ��������, ������� �������� ����� ������������ ��������, ����� ��������� ������������ � ����������� ������� ��� ����� ��������.')
            time.sleep(2)
            start(message)
        elif (message.text == '������'):
            bot.send_message(message.chat.id,
                             '������� ������� ������������ - ������� backend �����������, ������� �������� � ����� IT ��� ����� ���. �� ���������������� �� backend ����������, � ��� ���� � ������ � ���� ������� �������� ��������� ��������� ������ � ��� �������. ������� ������� �������� ��������� � ������������� ������ ����������������, ����� ��� C#, CSS, JavaScript, TypeScript. �� ����� �������� ��������� �������� � ������� ��� ������ � �������������� ����� ������������ backend � frontend ���-����������. �� ��������� ������� ������������ � ������������� ������ � ����� ������. �� ������ ���� ����� � ����� ����������� ������� ������� �����, ��������� � backend �����������. ��� ������� ���������� ������� ��������� � �������������������. ������� ������� �������� ������ ������� �������������, � ��� ���������������� ������ � ������ �������� � ���������� �������� ��������� ��� ��������� ���������� ��������. �� ����� ����� �������� ������ �������� � ������ � ������� ������� �������, ����� ���������� ������ ��������� ��� �������. � �����, ������� ������� ������������ - ��� ������� � ����������� backend �����������, ������� �������� ����� ������������ �������� � �������� ��� �������� ������������������, ����������� � ������������� backend ������� ��� ����� �������� � �������.')
            time.sleep(2)
            start(message)
    except:
        bot.send_message(message.chat.id, '<b>�� �����!</b>', parse_mode='html')

@bot.message_handler(commands=['learning'])
def learning(message):
    try:
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton('�������� ����������������')
        btn2 = types.KeyboardButton('�������� ������ � ���������')
        btn3 = types.KeyboardButton('�������� ��������� ������������')
        markup.add(btn1, btn2, btn3)
        helo = f'<b>������c����, {message.from_user.first_name}! � ��� �� ������ ������������?</b>'
        bot.send_message(message.chat.id, helo, parse_mode='html', reply_markup=markup)
        bot.register_next_step_handler(message, select1)
    except:
        bot.send_message(message.chat.id, '<b>�� �����!</b>', parse_mode='html')

def select1(message):
    try:
        if (message.text == '�������� ������ � ���������'):
            markup = types.InlineKeyboardMarkup()
            btn1 = types.InlineKeyboardButton("�������", url='https://vc.ru/marketing/282775-kak-obshchatsya-s-klientami/')
            markup.add(btn1)
            bot.send_message(message.chat.id, "��� �������:", reply_markup=markup)
            time.sleep(2)
            start(message)
        elif (message.text == '�������� ��������� ������������'):
            markup = types.InlineKeyboardMarkup()
            btn1 = types.InlineKeyboardButton("�������", url='https://www.atlassian.com/ru/work-management/project-collaboration/')
            markup.add(btn1)
            bot.send_message(message.chat.id, "��� �������:", reply_markup=markup)
            time.sleep(2)
            start(message)
        elif (message.text == '�������� ����������������'):
            markup = types.InlineKeyboardMarkup()
            btn1 = types.InlineKeyboardButton("�������", url='https://pythontutor.ru/')
            markup.add(btn1)
            bot.send_message(message.chat.id, "��� �������:", reply_markup=markup)
            time.sleep(2)
            start(message)
    except:
        bot.send_message(message.chat.id, '<b>�� �����!</b>', parse_mode='html')

def productcs(message):
    try:
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton('������� ��������')
        btn2 = types.KeyboardButton('������ ��������')
        btn3 = types.KeyboardButton('���������� � ��������')
        markup.add(btn1, btn2, btn3)
        bot.send_message(message.chat.id, f'������ ��� �� ������', reply_markup=markup)
        bot.register_next_step_handler(message, info)
    except:
        bot.send_message(message.chat.id, '�� �����!', parse_mode='html')

def info(message):
    try:
        if (message.text == '������� ��������'):
            bot.send_message(message.chat.id, 'Telegram ���� ��� �������� ��� ���������� onboarding �����������')
            time.sleep(2)
            start(message)
        elif (message.text == '������ ��������'):
            bot.send_message(message.chat.id, '���������� Telegram �����')
            time.sleep(2)
            start(message)
        elif (message.text == '���������� � ��������'):
            bot.send_message(message.chat.id, 'BracerIncorporation - ��� ������� IT-��������, ������������������ �� ���������� �������� ����������, ������, ����� � ������ IT-������� ��� ��������� ��������. �������� ����� ����������������������� �����������, ������� ������� backend � frontend �������������, � ����� �������� project ���������. ������� ������������� BracerIncorporation, �� ����� � ������� backend ������������� �������� ��������� ��������������, �������� ������� �������� ������ � ����� � ��������� ������ ����������������, ����� ��� C#, CSS, JavaScript, TypeScript. ��� ������������� ������������������ � ������������� IT-�������, ��������������� ����������� � ��������� ��������. ������� frontend ����������� ������� ���� �������� � ������� BracerIncorporation �������� �� ���������� ��������-����� ��������, ����� ��� ��������� ����, ����� � ���������. ��� ���� � ��������� ������ ����������������, ����� ��� Python, C++ � Kotlin, ��������� ��� ��������� ������������� � ��������������� ������������� ����������, ��������������� ����������� �������� � ����������� ��������������� ����������.')
            time.sleep(2)
            start(message)
    except:
        bot.send_message(message.chat.id, '<b>�� �����!</b>', parse_mode='html')

bot.polling(none_stop=True)