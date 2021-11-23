import telebot
from telebot import types

token = ""
bot = telebot.TeleBot(token)

@bot.message_handler(commands=['start'])
def start(message):
    keyboard = types.ReplyKeyboardMarkup()
    keyboard.row("Хочу", "/help", "/Расписание")
    bot.send_message(message.chat.id, 'Привет! Хочешь узнать свежее расписание?', reply_markup=keyboard)

@bot.message_handler(commands=['help'])
def start_message(message):
    bot.send_message(message.chat.id, 'Я умею показывать расписание')

@bot.message_handler(commands=['Расписание'])
def start(message):
    keyboard = types.ReplyKeyboardMarkup()
    keyboard.row("Понедельник", "Вторник", "Среда", "Четверг", "Пятница", "Суббота")
    bot.send_message(message.chat.id, 'Расписание БВТ2105', reply_markup=keyboard)

@bot.message_handler(content_types=['text'])
def answer(message):
    if message.text.lower() == "хочу":
        bot.send_message(message.chat.id, 'Тогда тебе сюда – https://mtuci.ru/')
    if message.text.lower() == "понедельник":
        bot.send_message(message.chat.id, 'Верхняя и Нижняя недели')
        bot.send_message(message.chat.id, 'ВВИТ практика 9:30-11:05')
        bot.send_message(message.chat.id, 'КГ практ 11:20-12:55')
        bot.send_message(message.chat.id, 'Философия практ 13:10-14:45')
        bot.send_message(message.chat.id, 'Выч.Тех практ и лаб 15:25-17:00')
    if message.text.lower() == "вторник":
        bot.send_message(message.chat.id, 'Верхняя неделя = ничего')
        bot.send_message(message.chat.id, 'Нижняя неделя')
        bot.send_message(message.chat.id, 'ВВит лаб 13:10-14:45')
        bot.send_message(message.chat.id, 'ВВит лаб 15:25-17:00')
        bot.send_message(message.chat.id, 'ВВит лекц 17:15-18:50')
    if message.text.lower() == "среда":
        bot.send_message(message.chat.id, 'Нижняя неделя')
        bot.send_message(message.chat.id, 'Ин яз 9:30-11:05')
        bot.send_message(message.chat.id, 'Ин яз 11:20-12:55')
        bot.send_message(message.chat.id, 'Верхняя неделя')
        bot.send_message(message.chat.id, 'Философия лекция 13:10-14:45')
        bot.send_message(message.chat.id, 'Кг лекция 15:25-17:00')
    if message.text.lower() == "четверг":
        bot.send_message(message.chat.id, 'Нижняя неделя')
        bot.send_message(message.chat.id, 'Информационная экология лекц 11:20-12:55')
        bot.send_message(message.chat.id, 'Информационная экология практика 15:25-17:00')
        bot.send_message(message.chat.id, 'Верхняя неделя')
        bot.send_message(message.chat.id, 'Алгебра и Геометрия лекц 15:25-17:00')
        bot.send_message(message.chat.id, 'Выш.мат лекц 17:15-18:50')
    if message.text.lower() == "пятница":
        bot.send_message(message.chat.id, 'Верхняя и Нижняя недели')
        bot.send_message(message.chat.id, 'Выч.тех лекц 11:20-12:55')
    if message.text.lower() == "суббота":
        bot.send_message(message.chat.id, 'Верхняя и Нижняя недели')
        bot.send_message(message.chat.id, 'Выш.мат практика 9:30-11:05')
        bot.send_message(message.chat.id, 'Алгебра и Геометрия практика 11:20-12:55')



bot.infinity_polling()