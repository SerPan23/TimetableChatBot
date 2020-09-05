from telebot import types
import db
teacher = False

markupClose = types.ReplyKeyboardRemove(selective=False)

BackKb = types.InlineKeyboardMarkup(row_width=1)
itembtn1 = types.InlineKeyboardButton('Назад', callback_data='back')
BackKb.add(itembtn1)


def select_action():
    if teacher:
        actionListKb = types.InlineKeyboardMarkup(row_width=1)
        timetableDay = types.InlineKeyboardButton(text='расписание на день', callback_data='timetableDay')
        timetableWeek = types.InlineKeyboardButton(text='расписание на неделю', callback_data='timetableWeek')
        timetableBuffet = types.InlineKeyboardButton(text='расписание буфета', callback_data='timetableBuffet')
        addHomework = types.InlineKeyboardButton(text='добавление домашнего задания', callback_data='addHomework')
        actionListKb.add(timetableDay, timetableWeek, timetableBuffet, addHomework)
    else:
        actionListKb = types.InlineKeyboardMarkup(row_width=1)
        timetableDay = types.InlineKeyboardButton(text='расписание на день', callback_data='timetableDay')
        timetableWeek = types.InlineKeyboardButton(text='расписание на неделю', callback_data='timetableWeek')
        homeworkDay = types.InlineKeyboardButton(text='домашнее задание на день', callback_data='homeworkDay')
        homeworkWeek = types.InlineKeyboardButton(text='домашнее задание на неделю', callback_data='homeworkWeek')
        timetableBuffet = types.InlineKeyboardButton(text='расписание буфета', callback_data='timetableBuffet')
        actionListKb.add(timetableDay, timetableWeek, homeworkDay, homeworkWeek, timetableBuffet)
    return actionListKb