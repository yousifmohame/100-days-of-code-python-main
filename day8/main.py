# ============ Day 8 ===============
# from art import logo

# def greet() :
#     print(3)
#     print(3)
#     print(3)

# greet()

# def greet_with_name(name):
#     print(f"hello {name}")
#     print(f"how are you {name}")

# greet_with_name("yousif")

# =====================
# Life in Weeks
# I was reading this article by Tim Urban - Your Life in Weeks and realised just how little time we actually have.
# Create a function called life_in_weeks() using maths and f-Strings that tells us how many weeks we have left, if we live until 90 years old.
# It will take your current age as the input and output a message with our time left in this format:
# You have x weeks left.
# Where x is replaced with the actual calculated number of weeks the input age has left until age 90.
# **Warning** The function must be called life_in_weeks for the tests to pass. 
# Also the output must have the same punctuation and spelling as the example. Including the full stop!
# Example Input
# 56

# Example Output
# You have 1768 weeks left.
# How to test your code and see your output?
# Udemy coding exercises do not have a console, so you cannot use input() . You will need to call your function with hard-coded values like so:

# def life_in_weeks(age):
#     x = ( (90-age) *52)
#     print(f"You have {x} weeks left")

# life_in_weeks(56)

# def greet_with (name, location):
#     print(f"hello {name}")
#     print(f"what is it like in {location}")

# greet_with(name="yousif", location="egypt")


# Love Calculator
# 💪 This is a difficult challenge! 💪 
# You are going to write a function called calculate_love_score() that tests the compatibility between two names.
# To work out the love score between two people: 
# 1. Take both people's names and check for the number of times the letters in the word TRUE occurs.   
# 2. Then check for the number of times the letters in the word LOVE occurs.   
# 3. Then combine these numbers to make a 2 digit number and print it out. 
# e.g.

# name1 = "Angela Yu" name2 = "Jack Bauer"
# T occurs 0 times 
# R occurs 1 time 
# U occurs 2 times 
# E occurs 2 times 

# Total = 5 
# L occurs 1 time 
# O occurs 0 times 
# V occurs 0 times 
# E occurs 2 times 
# Total = 3 
# Love Score = 53

# Example Input 
# calculate_love_score("Kanye West", "Kim Kardashian")
# Example Output
# 42

# def calculate_love_score(name1, name2):
#     combined_names = name1+name2
#     lower_names = combined_names.lower()

#     t = lower_names.count("t")
#     r = lower_names.count("r")
#     u = lower_names.count("u")
#     e = lower_names.count("e")

#     first_digit = t + r + u + e

#     l = lower_names.count("l")
#     o = lower_names.count("o")
#     v = lower_names.count("v")
#     e = lower_names.count("e")
#     second_digit = l + o + v + e
    
    
#     score = int(str(first_digit) + str(second_digit))
#     print(score)

# calculate_love_score("Kanye West", "Kim Kardashian")

# alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
# print(logo)
# end = True

# def ceaser(user_choise, original_text, shift_amount):
#     new_text =""
#     if user_choise == "decode" :
#         shift_amount *= -1
#     for char in original_text:
#         if char not in alphabet :
#             new_text += char
#         else :
#             num_alpha = alphabet.index(char) + shift_amount
#             num_alpha %= len(alphabet)
#             new_text += alphabet[num_alpha]
#     print(f"Here is the {user_choise} result: {new_text}")

# while end :
#     direcation = input("Type 'encode' to encrypt, type 'decode' to decrypt: \n").lower()
#     text = input("Type your message: \n").lower()
#     shift = int(input("Type the shift number: \n").lower())
    
#     ceaser(direcation, text, shift)
#     power = input("Type 'yes' if you want to go again. Otherwise type 'no' . \n").lower()
#     if power == "no" :
#         end = False
#         print("Goodbye")

# def shift_letter(letter, shift=2):
#     alpha = "abcd"
#     new_index = (alpha.index(letter) + shift) % len(alpha)
#     return alpha[new_index]

# print(shift_letter("c")) # a
# print(shift_letter(shift=-1, letter="a")) # d
# print("" in "caesar") # True

#في الكود أعلاه، لماذا عملت shift_letter("c") رغم أننا مررنا وسيطاً واحداً فقط ولم نمرر قيمة لـ shift؟ وماذا نسمي طريقة التمرير في السطر الثاني shift_letter(shift=-1, letter="a")؟
# because shift have initial value = 2 if not send value to shift and the second print name is keyword arguments

# الجملة الخاطئة 1: She is studies Python every day. 👈 الصح: she studies Python every day
# الجملة الخاطئة 2: What is your sister do? 👈 الصح: what is your sister doing?

