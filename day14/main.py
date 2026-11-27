# # =============== Day 14 ===============
# import random
# from art import logo, vs
# from game_data import data

# def make_options():
#     data_obj = random.choice(data)
#     random_option_ = data_obj
#     return random_option_

# def format_option(a):
#     return (f"{a['name']}, a {a['description']}, from {a['country']}.")

# def check_answer(a, b, answer):
#     if a['follower_count'] == b['follower_count']:
#         return True
#     elif a['follower_count'] > b['follower_count']:
#         return answer == "a"
#     else :
#         return answer == "b"

# def play():
#     score = 0
#     print(logo)
#     b = make_options()
#     while True:
#         a = b
#         b = make_options()
#         while a == b :
#             b = make_options()
        
#         print(f"Compare A: {format_option(a)}")
#         print(vs)
#         print(f"Compare B: {format_option(b)}")
#         answer = input("Who has more followers? Type 'A' or 'B': ").lower()
#         if answer == "a" or answer == "b":
#             result = check_answer(a, b, answer)
#             if result == True:
#                 score += 1
#                 print("\n"*20)
#                 print(f"You're right! Current score: {score}")   
#             else :
#                 print("\n"*20)
#                 print(f"Sorry, that's wrong. Final score: {score}")
#                 break
#         else :
#             print("wrong choice!")
#             break

# play()

# year = int(input("What's your year of birth? "))
# if year > 1980 and year < 1994:
#     print("You are a millennial.")
# elif year > 1994:
#     print("You are a Gen Z.") # not print anything because it out of the range compare and we can fix it when add = to condition 

# if user_guess == "a":
#     return True
# else:
#     return False ====== because if user input another word he look her b