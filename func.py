import telebot
import kb
import settings as se
import db

bot = telebot.TeleBot(se.TOKEN)


def send_day_lessons(message):
    bot.send_message(message.chat.id, "Расписание:", reply_markup=kb.BackKb)


def send_week_lessons(message):
    pass


def send_day_hw(message):
    pass


def send_week_hw(message):
    pass

