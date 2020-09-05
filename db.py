import json
import datetime
import db_setup
with open("data_file.json", "r") as read_file:
    data = json.load(read_file)

def send_day_lessons():
    return data["student_lessons"][f"{datetime.date.today()}"]


def send_week_lessons():
    pass


def send_day_hw():
    pass


def send_week_hw():
    pass

print(send_day_lessons())