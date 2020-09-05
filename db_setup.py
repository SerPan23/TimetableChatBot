import json

data = {
    "student_lessons": {
        "0": [{
            "date": "06.09.2020",
            "name": "Test lesson 1",
            "HW": "None"
        }],
        "1": [{
            "date": "05.09.2020",
            "name": "Test lesson 1",
            "HW": "None"
        }],
    }
}

with open("data_file.json", "w") as write_file:
    json.dump(data, write_file)