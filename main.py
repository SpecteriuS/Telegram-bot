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
        bot.send_message(message.chat.id, 'Верхняя и Нижняя недели'
                                            '\nВВИТ практика 9:30-11:05'
                                            '\nКГ практ 11:20-12:55'
                                            '\nФилософия практ 13:10-14:45'
                                            '\nВыч.Тех практ и лаб 15:25-17:00')
    if message.text.lower() == "вторник":
        bot.send_message(message.chat.id, 'Верхняя неделя = ничего')
        bot.send_message(message.chat.id, 'Нижняя неделя'
                                              '\nВВит лаб 13:10-14:45'
                                              '\nВВит лаб 15:25-17:00'
                                              '\nВВит лекц 17:15-18:50')
    if message.text.lower() == "среда":
        bot.send_message(message.chat.id, 'Нижняя неделя'
                                            '\nИн яз 9:30-11:05'
                                            '\nИн яз 11:20-12:55')
        bot.send_message(message.chat.id, 'Верхняя неделя'
                                              '\nФилософия лекция 13:10-14:45'
                                              '\nКг лекция 15:25-17:00')
    if message.text.lower() == "четверг":
        bot.send_message(message.chat.id, 'Нижняя неделя'
                                            '\nИнформационная экология лекц 11:20-12:55'
                                            '\nИнформационная экология практика 15:25-17:00')
        bot.send_message(message.chat.id, 'Верхняя неделя'
                                            '\nАлгебра и Геометрия лекц 15:25-17:00'
                                            '\nВыш.мат лекц 17:15-18:50')
    if message.text.lower() == "пятница":
        bot.send_message(message.chat.id, 'Верхняя и Нижняя недели'
                                           '\nВыч.тех лекц 11:20-12:55')
    if message.text.lower() == "суббота":
        bot.send_message(message.chat.id, 'Верхняя и Нижняя недели'
                                            '\nВыш.мат практика 9:30-11:05'
                                            '\nАлгебра и Геометрия практика 11:20-12:55')




bot.infinity_polling()
