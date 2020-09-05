import json

data = {
    "student_lessons": {
        "2020-09-05": {
            "HW": {
                "lesson1": "балдеж",
                "lesson2": "балдеж2"
            },
            "lessons":
                {
                    "math": "9:00",
                    "english": "10:00"
                }
        },
        "2020-09-06": {
            "HW": {
                "lesson1": "балдеж",
                "lesson2": "балдеж2"
            },
            "lessons":
                {
                    "math": "9:00",
                    "english": "10:00"
                }
        }

    },
    "all_days": {
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
}
parsed_string = json.dumps(data)
with open("data_file.json", "w") as write_file:
    json.dump(data, write_file)


def add_day(date, day):
    global data
    data["student_lessons"] = {
        f"{date}": {"HW": {}, "lesson": {f"{data['all_days'][f'{day}']}"}}}


add_day("2020-09-07", 3)
