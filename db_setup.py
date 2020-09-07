# import json
#
# allDays = {
#     "0":
#         {
#             "math": "9:00",
#             "english": "10:00"
#
#         },
#     "1":
#         {
#             "math": "9:00",
#             "english": "10:00"
#
#         },
#     "2":
#         {
#             "math": "9:00",
#             "english": "10:00"
#
#         },
#     "3":
#         {
#             "math": "9:00",
#             "english": "10:00"
#
#         },
#     "4":
#         {
#             "math": "9:00",
#             "english": "10:00"
#
#         }
#
# }
#
#
# # "2020-09-06": {
# #     "HW": {
# #         "lesson1": "балдеж",
# #         "lesson2": "балдеж2"
# #     },
# #     "lessons":
# #         {
# #             "math": "9:00",
# #             "english": "10:00"
# #         }
# # }
#
# def add_day(date, day):
#     global allDays
#     k = {date: {"HW": {}, "lesson": f"{allDays.get(f'{day}')}"},}
#     with open("student_lessons.json", "a") as write_file:
#         json.dump(k, write_file)
#
#
# add_day("2020-09-11", 4)
# # data["student_lessons"] = {
# #     date: {"HW": {}, "lesson": {f"{data['all_days'][f'{day}']}"}}}
