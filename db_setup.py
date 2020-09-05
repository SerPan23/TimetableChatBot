import json

data = {
    "student_lessons": {
        "2020-09-05": [
            {

                "HW": [
                    {
                        "lesson1": "балдеж",
                        "lesson2": "балдеж2"
                    }
                ],
                "lessons": [
                    {
                        "math": "9:00",
                        "english": "10:00"
                    }
                ]
            }
        ],
        "1": [
            {
                "date": "2020-09-05",
                "HW": [
                    {
                        "lesson1": "балдеж",
                        "lesson2": "балдеж2"
                    }
                ],
                "lessons": [
                    {
                        "math": "9:00",
                        "english": "10:00"
                    }
                ]
            }
        ]

    }
}
parsed_string = json.dumps(data)
with open("data_file.json", "w") as write_file:
    json.dump(data, write_file)
