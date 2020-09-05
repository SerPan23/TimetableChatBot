import db
import kb
import settings as se
import telebot
import func as f
bot = telebot.TeleBot(se.TOKEN)


@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.send_message(message.chat.id,
                     "Выбери действие", reply_markup=kb.markupClose)
    items = db.show_all_lessons()
    for i in items:
        bot.send_message(message.chat.id, text=i)


bot.enable_save_next_step_handlers(delay=2)
bot.load_next_step_handlers()
bot.polling(none_stop=True, interval=0)

