import pymongo
import settings as se
import datetime

mdb = pymongo.MongoClient(se.MONGODB_LINK)[se.MONGO_DB]

def add_day(date, day):
    allDay = mdb.all_days
    days = {date: {"HW": {}, "lesson": {f"{allDay}": f'{day}'}}}
    add = mdb.student_lesson
    add.insert_one(days).inserted_id


def add_hw():
    pass


def send_day_lessons():
    pass


def send_week_lessons():
    pass


def send_day_hw():
    pass


def add_lesson():
    day = {}
    allDay = mdb.student_lesson
    allDay.insert_one().inserted_id


add_day(datetime.date.today(), 3)
# def give_lessons():
#     l = []
#     for i in mdb.lessons.find():
#         l.append(i)
#     return l
