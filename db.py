import pymongo
import settings as se

mdb = pymongo.MongoClient(se.MONGODB_LINK)[se.MONGO_DB]


def add_day():
    pass


def add_hw():
    pass


def send_day_lessons():
    pass


def send_week_lessons():
    pass


def send_day_hw():
    pass


def add_lesson():
    allDays = {
        "0":
            {
                "math": "9:00",
                "english": "10:00"

            },
        "1":
            {
                "math": "9:00",
                "english": "10:00"

            },
        "2":
            {
                "math": "9:00",
                "english": "10:00"

            },
        "3":
            {
                "math": "9:00",
                "english": "10:00"

            },
        "4":
            {
                "math": "9:00",
                "english": "10:00"

            }

    }
    allDay = mdb.all_days
    allDay.insert_one(allDays).inserted_id
add_lesson()
# def give_lessons():
#     l = []
#     for i in mdb.lessons.find():
#         l.append(i)
#     return l
