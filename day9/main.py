# =============== Day 9 ===============
# from art import logo
# Grading Program
# You have access to a database of student_scores in the format of a dictionary.
# The keys in student_scores are the names of the students and the values are their exam scores. 
# Write a program that converts their scores to grades.
# By the end of your program, you should have a new dictionary called student_grades that should
# contain student names as keys and their assessed grades for values. 

# The final version of the student_grades dictionary will be checked. 

# **DO NOT** modify lines 1-7 to change the existing student_scores dictionary. 
# This is the scoring criteria: 
# - Scores 91 - 100: Grade = "Outstanding" 
# - Scores 81 - 90: Grade = "Exceeds Expectations" 
# - Scores 71 - 80: Grade = "Acceptable" 
# - Scores 70 or lower: Grade = "Fail" 

# student_scores = {
#     'Harry': 88,
#     'Ron': 78,
#     'Hermione': 95,
#     'Draco': 75,
#     'Neville': 60
# }

# student_grades = {}

# for name in student_scores :
#     score = student_scores[name]
#     if score <= 70:
#         student_grades[name] = "Fail"
#     elif score >= 71 and score <= 80:
#         student_grades[name] = "Acceptable"
#     elif score >= 81 and score <= 90:
#         student_grades[name] = "Exceeds Expectations"
#     elif score >= 91 and score <= 100:
#         student_grades[name] = "Outstanding"
#     else :
#         print("wrong")
# print(student_grades)

# travel_log = {
#     "France" : ["Paris", "Lille", "Dijon"]
# }
# print(travel_log["France"][1])

# nested_list = ["A", "B", ["C", "D"]]
# print(nested_list[2][1])

# travel_log = {
#     "France" : {
#         "cities_visited" : ["Paris", "Lille", "Dijon"]
#     }
# }

# print(travel_log["France"]["cities_visited"][2])
# print(logo)
# restart = True
# max_num = 0
# bidding = {}
# while restart :
#     user_name = input("What is your name?: ").lower()
#     bid_num = int(input("What is your bid?: $ "))
#     new_bid = input("Are there any other bidders? Type 'yes or 'no'. \n").lower()
#     bidding[user_name] = bid_num
#     if new_bid == "no" :  
#         for bid in bidding:
#             price = bidding[bid]
#             if price >= max_num :
#                 max_num = price
#                 win_name = bid
#         restart = False
#     else :
#         print("\n" * 100)

# print(f"The winner is {win_name} with a bid of ${max_num}")