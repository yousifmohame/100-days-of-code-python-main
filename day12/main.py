# import random
# from art import logo

# # 1. الثوابت العامة في أعلى الملف (Global Constants)
# EASY_LEVEL_TURNS = 10
# HARD_LEVEL_TURNS = 5

# def set_difficulty():
#     """Asks the user for difficulty and returns the corresponding number of turns."""
#     while True:
#         level = input("Choose a difficulty. Type 'easy' or 'hard': ").strip().lower()
#         if level == "easy":
#             return EASY_LEVEL_TURNS
#         elif level == "hard":
#             return HARD_LEVEL_TURNS
#         else:
#             print("Invalid choice! Please type 'easy' or 'hard'.")

# def check_guess(user_guess, actual_answer, turns):
#     """Checks answer against guess, and returns the remaining turns."""
#     if user_guess > actual_answer:
#         print("Too high.")
#         return turns - 1
#     elif user_guess < actual_answer:
#         print("Too low.")
#         return turns - 1
#     else:
#         print(f"You got it! The answer was {actual_answer}.")
#         return turns

# def game():
#     print(logo)
#     print("Welcome to the Number Guessing Game!")
#     print("I'm thinking of a number between 1 and 100.")

#     answer = random.randint(1, 100)
#     turns = set_difficulty()
#     guess = None

#     while guess != answer:
#         print(f"You have {turns} attempts remaining to guess the number.")
#         guess = int(input("Make a guess: "))

#         # نفحص الفوز والتخمين قبل إعلان الخسارة
#         turns = check_guess(guess, answer, turns)

#         if guess == answer:
#             return  # ينهي اللعبة فوراً عند الفوز حتى لو كانت المحاولة الأخيرة
#         elif turns == 0:
#             print(f"You've run out of guesses, you lose. The answer was {answer}.")
#             return
#         else:
#             print("Guess again.")

# game()

# # --- المقطع أ ---
# enemies = 1
# def increase_enemies():
#     enemies = 2
#     print(f"Inside: {enemies}")

# increase_enemies()  # Inside: 2
# print(f"Outside: {enemies}") # Outside: 1

# # --- المقطع ب ---
# score = 10
# def add_point():
#     score += 1  # انتبه لهذا السطر جيداً!
#     return score

# print(add_point()) # UnboundLocalError: cannot access local variable 'score' where it is not associated with a value

# In my first version, the player could not win on the last attempt because the code make retry_num -= 1 first and if the user correct not calcute in result
# Where you live? 👈 الصح: Where do you live?

# Why he is late? 👈 الصح: Why is he late?

# How much attempts are left? 👈 الصح: How many attempts are left?