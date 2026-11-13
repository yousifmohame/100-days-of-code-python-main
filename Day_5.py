# ============ Day 5 ===============
# import random
# 1- for loop

# fruits = ["Apple", "Peach", "Pear"]

# for fruit in fruits :
#     print(fruit)

# student_scores = [188, 170, 166, 189, 190, 146, 135, 136, 199, 210, 120]

# sum_student_score = sum(student_scores)
# print(sum_student_score)

# sum = 0
# for score in student_scores :
#     sum += score
# print(sum)

# max_student_score = max(student_scores)
# print(max_student_score)

# max_score = 0

# for score in student_scores :
#     if score > max_score :
#         max_score = score

# print(max_score)

# sum_num=0
# for number in range(1, 101):
#     sum_num += number

# print(sum_num)

# FizzBuzz
# You are going to write a program that automatically prints the solution to the FizzBuzz game. 
# These are the rules of the FizzBuzz game:
# Your program should print each number from 1 to 100 in turn and include number 100.
# But when the number is divisible by 3 then instead of printing the number it should print "Fizz".
# When the number is divisible by 5, then instead of printing the number it should print "Buzz".`
# And if the number is divisible by both 3 and 5 e.g. 15 then instead of the number it should print "FizzBuzz"
# e.g. it might start off like this:

# for number in range(1, 101):
#     if number % 3 == 0 and number % 5 ==0 :
#         print("FizzBuzz")
#     elif number % 3 == 0 :
#         print("Fizz")
#     elif number % 5 == 0 :
#         print("Buzz")
#     else :
#         print(number)

# letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
# numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
# symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

# print("Welcome to the PyPassword Generator!")
# nr_letters= int(input("How many letters would you like in your password?\n"))
# nr_symbols = int(input(f"How many symbols would you like?\n"))
# nr_numbers = int(input(f"How many numbers would you like?\n"))

# random_letters = []
# random_numbers = []
# random_symbols = []

# for letter in range(0, len(letters)) :
#     random_letter_num = random.randint(0, (len(letters)-1)) 
#     random_numbers_num = random.randint(0, (len(numbers)-1)) 
#     random_symbols_num = random.randint(0, (len(symbols)-1))
#     random_letters.append(letters[random_letter_num])
#     random_numbers.append(numbers[random_numbers_num])
#     random_symbols.append(symbols[random_symbols_num])

# user_num_letters = random_letters[:nr_letters]
# user_num_numbers = random_numbers[:nr_numbers]
# user_num_symbols = random_symbols[:nr_symbols]

# all_password = [user_num_letters , user_num_numbers , user_num_symbols]

# all_password_words =[]

# for password in all_password :
#     for password_words in password :
#         all_password_words.append(password_words)

# random.shuffle(all_password_words)

# final_password = ""

# for wordspass in all_password_words:
#     final_password += wordspass
# print(final_password)

# letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
# numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
# symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

# print("Welcome to the PyPassword Generator!")
# nr_letters= int(input("How many letters would you like in your password?\n"))
# nr_symbols = int(input(f"How many symbols would you like?\n"))
# nr_numbers = int(input(f"How many numbers would you like?\n"))

# password=[]

# for _ in range(nr_letters) :
#     password.append(random.choice(letters))

# for _ in range(nr_symbols) :
#     password.append(random.choice(symbols))

# for _ in range(nr_numbers) :
#     password.append(random.choice(numbers))

# random.shuffle(password)
# finalpassword = "".join(password)

# print(finalpassword)


# print(list(range(2, 10, 3))) # [2, 5, 8] because range take (start point, end point, number steps to + )
# print(["a", "b"] + ["c", "d"]) # ["a", "b", "c", "d"] because + make combination to lists
# print("-".join(["2026", "10", "08"])) # 2026-10-08 because join make loop on list and add - in every loop


# لديك قائمة درجات حرارة تحت الصفر:temperatures = [-12, -5, -20, -3, -15]
# اكتب كود حلقة for يطبع أعلى درجة حرارة (أكبر رقم، وهو هنا -3) وأقل درجة حرارة (أصغر رقم، وهو هنا -20)
# بدون استخدام دالتي max() أو min() الجاهزتين، وبدون الوقوع في فخ البدء من الصفر 0!

# temperatures = [-12, -5, -20, -3, -15]

# maxtemp = temperatures[-1]
# lowtemp = temperatures[-1]
# for temp in temperatures :
#     if temp > maxtemp:
#         maxtemp = temp
#     elif temp < lowtemp :
#         lowtemp = temp

# print(maxtemp)
# print(lowtemp)

# The password_list is empty.

# Letters and numbers are inside the list.

# I am building a password generator.

# In the FizzBuzz game, if a number is divisible by both 3 and 5, the program prints FizzBuzz , and if a number is divisible by 3, program prints Fizz ,and if a number is divisible by 5, program prints Buzz , if else, program prints the number

# We must check this condition first because if works with condition baskliy