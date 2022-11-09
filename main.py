from telebot.types import User
import requests
import telebot

from telebot import types
from telebot import custom_filters
# from telebot import types

myid = '936793854'

"""r2 = requests.get(
        'https://api.telegram.org/bot5584840403:AAHLSIaM3QhPdffPrBW50EvHSQzw2YUqELE/getMe')
    # print(r2.text)
    r3 = requests.post(
        'https://api.telegram.org/bot5584840403:AAHLSIaM3QhPdffPrBW50EvHSQzw2YUqELE/sendMessage',
        data={'chat_id': myid, 'text': 'Привет! Я бот для поиска мест г.Барнаула'})
    # print(r3.text)
    r4 = requests.get(
        "https://api.telegram.org/bot5584840403:AAHLSIaM3QhPdffPrBW50EvHSQzw2YUqELE/getUpdates")
    # print(r4.text)"""

cmd = []
temp=[]
bot = telebot.TeleBot('5584840403:AAHLSIaM3QhPdffPrBW50EvHSQzw2YUqELE', parse_mode=None)


@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
    bot.reply_to(message,
                 "Привет! Я помогу найти тебе красивое место для прогулки. Выбери одно из мест.")


@bot.message_handler(commands=['Место1'])
def send_welcome(message):
    print(message)
    bot.reply_to(message,
                 "Площадь мира,Ленинский район,13 положительных отзывов,Красивое место")
    bot.send_photo(myid, photo=(
        'https://barnaul.org/upload/resize_cache/iblock/f06/1140_670_11ad056af159509fa29b13aa1d5079c1a/DSC_8634.jpg'))


@bot.message_handler(commands=['Место2'])
def send_welcome(message):
    bot.reply_to(message,
                 "Горная аптека г.Барнаула, Центральный район,ул.Пушкина д.Колотушкина, 10 положительных отзывов ")
    bot.send_photo(myid, photo=(
        'https://visitaltai.info/upload/resize_cache/iblock/251/466_302_2/251281da2c06c906578960b86cf6b66b.jpg'))


@bot.message_handler(commands=['Место3'])
def send_welcome(message):
    print(message)
    id = str(message)
    print(type(id))
    print(id)
    bot.reply_to(message,
                 "Мусорный бак на ул.Шукшина, Октябрьский район, 25 отрицательных отзывов")
    bot.send_photo(myid, photo=(
        'https://s.poembook.ru/theme/f0/7b/98/8f72c0097be7e591323cf05632d565a2b5a73f78.jpeg'))


markup = types.ReplyKeyboardMarkup()
itembtna = types.KeyboardButton('/Место1')
itembtnv = types.KeyboardButton('/Место2')
itembtnc = types.KeyboardButton('/Место3')
markup.row(itembtna, itembtnv)
markup.row(itembtnc)
bot.send_message(myid, "Выбери одно из мест:", reply_markup=markup)


@bot.message_handler(commands=['add'])
def send_welcome(message):
    id = message('from_user')
    id = id('id')
    print(id)
    bot.reply_to(message,
                 "Мусорный бак на ул.Шукшина, Октябрьский район, 25 отрицательных отзывов")
    bot.send_photo(myid, photo=(
        'https://s.poembook.ru/theme/f0/7b/98/8f72c0097be7e591323cf05632d565a2b5a73f78.jpeg'))

@bot.message_handler(chat_id=[936793854], commands=['Добавить']) # chat_id checks id corresponds to your list or not.
def admin_rep(message):
    bot.send_message(message.chat.id, "allowed")
    msg =  bot.reply_to(message,"Введите название улицы")
    bot.register_next_step_handler(msg, area)


def area(message):
    try:

        temp.append(message.text)

        #         user_dict[chat_id] = user
        msg = bot.reply_to(message, 'Назовите адрес')
        bot.register_next_step_handler(msg, location)
    except Exception as e:
        bot.reply_to(message, 'oooops')
def location(message):
    try:

        temp.append(message.text)
        print(cmd)
        msg = bot.reply_to(message, 'Кол-во положительных отзывов')
        bot.register_next_step_handler(msg, comments)
    except Exception as e:
        bot.reply_to(message, 'oooops')


def comments(message):
    try:
        msg = bot.reply_to(message, 'Кол-во положительных отзывов')
        temp.append(message.text)
        cmd.append(temp)
        print(cmd)
        #         user_dict[chat_id] = user
        msg = bot.reply_to(message, 'Добавлено')
        #                bot.register_next_step_handler(msg, process_age_step)
    except Exception as e:
        bot.reply_to(message, 'oooops')


@bot.message_handler(commands=['Добавить'])
def not_admin(message):
    bot.send_message(message.chat.id, "You are not allowed to use this command")

# Do not forget to register
bot.add_custom_filter(custom_filters.ChatFilter())


@bot.message_handler(func=lambda m: True)
def echo_all(message):
    bot.reply_to(message, 'Ошибка: Неверная команда. Напиши /help')


bot.enable_save_next_step_handlers(delay=2)

# Load next_step_handlers from save file (default "./.handlers-saves/step.save")
# WARNING It will work only if enable_save_next_step_handlers was called!
bot.load_next_step_handlers()
bot.infinity_polling()
