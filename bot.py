import telebot
import configure
from telebot import types
from telegram.ext import Updater, CommandHandler, CallbackQueryHandler
from telegram import InlineKeyboardButton, InlineKeyboardMarkup
from telegram_menu import BaseMessage, TelegramMenuSession
import webbrowser

client = telebot.TeleBot(configure.config['token'])

@client.message_handler(commands = ['get start', 'start'])
def get_user_info(message):
    markup_inline = types.InlineKeyboardMarkup()
    item_registration = types.InlineKeyboardButton(text='Daftar PMB', callback_data='daftar')
    item_information = types.InlineKeyboardButton(text='Informasi', callback_data='informasi')
    item_coba = types.InlineKeyboardButton(text='Coba', callback_data='coba')

    markup_inline.add(item_registration,item_information, item_coba)
    client.send_message(message.chat.id, 'Hai kamu, Selamat datang di Bachat Bot AMIKOM. Undang dan ajak teman-teman yang ingin mendaftar dan mengetahui info terkait Universitas AMIKOM Yogyakarta untuk menggunakan bot ini ya. Salam Bachat <3', reply_markup=markup_inline)

@client.callback_query_handler(func = lambda call:True)
def answer(call):
    if call.data == 'daftar':
        markup_reply = types.ReplyKeyboardMarkup(resize_keyboard=True)
        item_d3s1 = types.KeyboardButton ('D3&S1')
        item_magister = types.KeyboardButton('Magister(S2)')

        markup_reply.add(item_d3s1, item_magister)
        client.send_message(call.message.chat.id, 'Klik tombol sesuai pendaftaran yang akan di submit', reply_markup=markup_reply)

    elif call.data == 'informasi':
        markup_reply = types.ReplyKeyboardMarkup(resize_keyboard=True)
        item_info1 = types.KeyboardButton ('Info1')
        item_info2 = types.KeyboardButton('Info2')
        item_info3 = types.KeyboardButton('Info3')

        markup_reply.add(item_info1, item_info2, item_info3)
        client.send_message(call.message.chat.id, 'Klik tombol sesuai pendaftaran yang akan di submit', reply_markup=markup_reply)

    elif call.data == 'coba':
        markup_reply = types.ReplyKeyboardMarkup(resize_keyboard=True)
        item_coba = types.KeyboardButton ('Coba')

        markup_reply.add(item_coba)
        client.send_message(call.message.chat.id, 'Klik tombol sesuai pendaftaran yang akan di submit', reply_markup=markup_reply)

@client.message_handler(content_types = ['text'])
def get_text(message):
    if message.text == 'D3&S1':
        client.send_message(message.chat.id, f'Kamu bisa mengunjungi : https://bit.ly/D3danS1')
    elif message.text == 'Magister(S2)':
        client.send_message(message.chat.id, f'Kamu bisa mengunjungi : https://bit.ly/TeknikInformatikaProgramMagister')
    elif message.text == 'Info1':
        client.send_message(message.chat.id, f'Testinfo1')
    elif message.text == 'Info2':
        client.send_message(message.chat.id, f'Testinfo2')
    elif message.text == 'Info3':
        client.send_message(message.chat.id, f'Testinfo3')
    elif message.text == 'Coba':
        client.send_message(message.chat.id, f'Cobaaaaaaaacok')
    

"""
@client.message_handler(content_types = ['text'])
def get_text(message):
    if message.text.lower() == 'bachat':
        client.send_message(message.chat.id, "Hai kamu, Selamat datang di Bachat Bot AMIKOM. Undang dan ajak teman-teman yang ingin mendaftar dan mengetahui info terkait Universitas AMIKOM Yogyakarta untuk menggunakan bot ini ya. Salam Bachat <3")
"""
client.polling(none_stop = True, interval = 0)

