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
        },
        "all_days":{
            "monday":
                {
                    "math": "9:00",
                    "english": "10:00"

                },
            "thuesday":
                {
                    "math": "9:00",
                    "english": "10:00"

                },
            "wendsday":
                {
                    "math": "9:00",
                    "english": "10:00"

                }


        }

    }
}
parsed_string = json.dumps(data)
with open("data_file.json", "w") as write_file:
    json.dump(data, write_file)
