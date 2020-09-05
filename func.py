import telebot
import kb
import settings as se
import db

bot = telebot.TeleBot(se.TOKEN)


def send_day_lessons(message):
    bot.send_message(message.chat.id, "Расписание:", reply_markup=kb.BackKb)


def send_week_lessons(message):
    bot.send_message(message.chat.id, "Расписание на неделю:", reply_markup=kb.BackKb)


def send_day_hw(message):
    bot.send_message(message.chat.id, "Домашка:", reply_markup=kb.BackKb)


def send_week_hw(message):
    bot.send_message(message.chat.id, "Домашка на неделю:", reply_markup=kb.BackKb)

