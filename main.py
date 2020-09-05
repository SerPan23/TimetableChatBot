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
        f.send_day_lessons(call.message)
    elif call.data == "timetableWeek":
        f.send_week_lessons(call.message)
    elif call.data == "homeworkDay":
        f.send_day_hw(call.message)
    elif call.data == "homeworkWeek":
        f.send_week_hw(call.message)
    elif call.data == "timetableBuffet":
        pass
    elif call.data == "addHomework":
        pass


@bot.message_handler(func=lambda message: True)
def callback_msg(message):
    if message.text == 'Назад':
        send_welcome(message)


bot.enable_save_next_step_handlers(delay=2)
bot.load_next_step_handlers()
bot.polling(none_stop=True, interval=0)
