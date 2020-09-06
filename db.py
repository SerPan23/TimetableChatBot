import json
import datetime
import settings as se
import pymongo as pymongo

import db_setup as dbs

mdb = pymongo.MongoClient(se.MONGODB_LINK)[se.MONGO_DB]

with open("student_lessons.json", "r") as read_file:
    data = json.load(read_file)


def send_day_lessons():
    return data[f"{datetime.date.today()}"]['lessons']


def send_week_lessons():
    return dbs.allDays


def send_day_hw(day):
    return data[f"{day}"]["HW"]


print(send_day_hw())
