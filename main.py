import db
import kb
import settings as se
import telebot
import func as f
bot = telebot.TeleBot(se.TOKEN)


@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.send_message(message.chat.id,
                     "Выбери действие:", reply_markup=kb.select_action())


@bot.callback_query_handler(func=lambda call: True)
def callback_worker(call):
    if call.data == "timetableDay":
        pass
    elif call.data == "timetableWeek":
        pass
    elif call.data == "homeworkDay":
        pass
    elif call.data == "homeworkWeek":
        pass
    elif call.data == "timetableBuffet":
        pass
    elif call.data == "addHomework":
        pass


bot.enable_save_next_step_handlers(delay=2)
bot.load_next_step_handlers()
bot.polling(none_stop=True, interval=0)

