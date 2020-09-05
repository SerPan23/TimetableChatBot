import json
import datetime

with open("data_file.json", "r") as read_file:
    data = json.load(read_file)


def send_day_lessons():
    return data["student_lessons"][f"{datetime.date.today()}"]['lessons']


def send_week_lessons():
    return data["all_days"]


def send_day_hw(day):
    return data["student_lessons"][f"{day}"]["HW"]
