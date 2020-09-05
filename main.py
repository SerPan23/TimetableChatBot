import db
import kb
import settings as se
import telebot
bot = telebot.TeleBot(se.TOKEN)


@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.send_message(message.chat.id,
                     "Выбери действие:", reply_markup=kb.select_action())


@bot.callback_query_handler(func=lambda call: True)
def callback_worker(call):
    if call.data == "timetableDay":
        send_day_lessons(call.message)
    elif call.data == "timetableWeek":
        send_week_lessons(call.message)
    elif call.data == "homeworkDay":
        # f.send_day_hw(call.message)
        m = bot.send_message(call.message.chat.id, "Напишите номер дня.месяца:")
        bot.register_next_step_handler(m, get_day_num)

    elif call.data == "timetableBuffet":
        pass
    elif call.data == "addHomework":
        pass
    elif call.data == "back":
        send_welcome(call.message)


@bot.message_handler(func=lambda message: True)
def callback_msg(message):
    if message.text == 'Назад':
        send_welcome(message)


def get_day_num(message):
    dn = message.text
    if len(dn) == 5:
        f = dn[0]+dn[1]
        t = dn[2]
        s = dn[3]+dn[4]
        if (int(f) >= 1 or int(f) <= 31) and t == "." and (int(s) >= 1 or int(s) <= 12):
            # print('yes')
            send_day_hw(message, dn)
        else:
            # print('no1')
            m = bot.send_message(message.chat.id, "Напишите номер дня.месяца (в формате 00.00):")
            bot.register_next_step_handler(m, get_day_num)
    else:
        # print('no2')
        m = bot.send_message(message.chat.id, "Напишите номер дня.месяца (в формате 00.00):")
        bot.register_next_step_handler(m, get_day_num)


def send_day_lessons(message):
    bot.send_message(message.chat.id, "Расписание:", reply_markup=kb.BackKb)


def send_week_lessons(message):
    bot.send_message(message.chat.id, "Расписание на неделю:", reply_markup=kb.BackKb)


def send_day_hw(message, dn):
    bot.send_message(message.chat.id, "Домашка: " + dn, reply_markup=kb.BackKb)


bot.enable_save_next_step_handlers(delay=2)
bot.load_next_step_handlers()
bot.polling(none_stop=True, interval=0)

