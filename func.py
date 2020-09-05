import telebot
import kb
import settings as se
import db

bot = telebot.TeleBot(se.TOKEN)

def send_all_lessons():
    return db.show_all_lessons()

