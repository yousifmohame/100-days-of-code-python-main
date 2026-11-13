# ============ Day 4 ===============
# import random

# interger_random = random.randint(111111, 999999)
# print(interger_random)

# random_number_0_10 = random.random() * 10
# print(random_number_0_10)

# random_float = random.uniform(0, 10)
# print(random_float)

# random_coin = random.randint(0, 1)
# if random_coin == 0 :
#     print("Head")
# else :
#     print("Tail")

# friends = ["Alice", "Bob", "Charlie", "David", "Emanuel"]
# random_friend_index = random.randint(0, 4)
# print(friends[random_friend_index])
# print(random.choice(friends))

# rock = '''
#     _______
# ---'   ____)
#       (_____)
#       (_____)
#       (____)
# ---.__(___)
# '''

# paper = '''
#     _______
# ---'   ____)____
#           ______)
#           _______)
#          _______)
# ---.__________)
# '''

# scissors = '''
#     _______
# ---'   ____)____
#           ______)
#        __________)
#       (____)
# ---.__(___)
# '''

# rock_baber= [rock, paper, scissors]

# user_input = int(input("what do you choose? Type 0 for Rock, 1 for Paper or 2 for Scrissors.\n"))

# if user_input == 0 :
#     print(rock_baber[0])
# elif user_input == 1 :
#     print(rock_baber[1])
# elif user_input == 2 :
#     print(rock_baber[2])
# else :
#     print("wrong choise")

# computer_choice = random.randint(0, 2)

# print("Computer Choise: ")
# if computer_choice == 0 :
#     print(rock_baber[0])
# elif computer_choice == 1 :
#     print(rock_baber[1])
# elif computer_choice == 2 :
#     print(rock_baber[2])
# else :
#     print("wrong choise")

# if user_input == computer_choice :
#     print("draw")
# elif user_input == 0 and computer_choice == 2 :
#     print("you win")
# elif user_input == 2 and computer_choice == 1 :
#     print("you win")
# elif user_input == 1 and computer_choice == 0 :
#     print("you win")
# else:
#     print("you loss")

# matrix = [
#     ["A", "B", "C"],
#     ["D", "E", "F"],
#     ["G", "H", "I"]
# ]
# print(matrix[1][2]) # C
# print(matrix[-1][0]) # G
# print(len(matrix)) # 3

# 1. من ثغرة المصفوفة اليوم: كيف نطبع الحرف "D" ثم الحرف "H" من هذه المصفوفة؟
# grid = [
#     ["A", "B", "C"],
#     ["D", "E", "F"],
#     ["G", "H", "I"]
# ]
# print(grid[1][0]) # نريد طباعة "D"
# print(grid[2][1]) # نريد طباعة "H"

# # 2. من ثغرات الأيام 1-3: ما ناتج كل سطر ولماذا؟
# print(int(9.99)) # 9 because int function return intger number only
# print(bool("")) # false because the empty string is false
# print(14 % 4) # 2 because 3 x 4 + 2 =14

# prices = [50.0, 80.0, 120.0]

# user_input = int(input("please enter 0 , 1 or 2 for meal \n"))

# if user_input < 0 or user_input > 2 :
#     print("invalid choice")
# else :
#     meal_price = prices[user_input]
#     if meal_price >= 100 :
#         dis_price = meal_price-(meal_price/10)
#         print(f"{dis_price:.2f}")
#     else :
#         print(f"{meal_price:.2f}")

# اختر a أو an (انتبه للصوت لا للحرف!):

# an integer (ينطق: إنتجر)

# a user (ينطق: يوزر)

# an honest developer (ينطق: أونيست — الـ h صامتة)

# a string (ينطق: سترينج)

# حول هاتين الجملتين من المفرد إلى الجمع (غيّر This/That والفعل والاسم):

# الجملة 1: This is a list. 👈 تصبح: these are lists

# الجملة 2: That is an error. 👈 تصبح: those are errors

