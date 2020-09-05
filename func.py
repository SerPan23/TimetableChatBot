import telebot
import kb
import settings as se
import db

bot = telebot.TeleBot(se.TOKEN)


def send_day_lessons(message):
    bot.send_message(message.chat.id, "Расписание:", reply_markup=kb.BackKb)


def send_week_lessons(message):
    bot.send_message(message.chat.id, "Расписание на неделю:", reply_markup=kb.BackKb)


def send_day_hw(message, dn):
    bot.send_message(message.chat.id, "Домашка: " + dn, reply_markup=kb.BackKb)


def get_day_num(message):
    dn = message.text
    
    send_day_hw(message, dn)
