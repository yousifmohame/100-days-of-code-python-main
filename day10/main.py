# =============== Day 10 ===============
from art import logo
# def format_name(fname, lname):
#     cleanname = fname.lower() + " " + lname.lower()
#     return cleanname.title()

# print(format_name("AHmed", "aLi"))

# def is_leap_year(year):
#     """this function make check year is leap or not"""
#     if (year % 4) == 0:
#         if (year % 100) == 0:
#             if (year % 400) == 0:
#                 return True
#             else:
#                 return False
#         else:
#             return True
#     else:
#         return False

# print(is_leap_year(1989))

# def add(n1, n2):
#     return n1 + n2
# def sub(n1, n2):
#     return n1 - n2
# def mul(n1, n2):
#     return n1 * n2
# def div(n1, n2):
#     return n1 / n2

# operations ={
#     "+": add,
#     "-": sub,
#     "*": mul,
#     "/": div,
# }

# start = True
# result = 0
# new_opearation = "n"

# while start :
#     if new_opearation == "n":
#         number1 = float(input("What's the first number?: "))
#     operation = input("+\n-\n*\n/\nPick an operation: \n")
#     number2 = float(input("What's the next number?: "))

#     if operation not in operations :
#         print("wrong operation!")
#     else:
#         result = operations[operation](number1, number2)
#     # if operation == "+" :
#     #     result = add(number1, number2)
#     # elif operation == "-" :
#     #     result = sub(number1, number2)
#     # elif operation == "*" :
#     #     result = mul(number1, number2)
#     # elif operation == "/" :
#     #     result = div(number1, number2)
#     # else:
#     #     print("wrong operation!")

#     print(f"{number1} {operation} {number2} = {result}")

#     new_opearation = input(f"Type 'y' to continue calculating with {result}, or type 'n' to start a new calculation, or 'end' to end: ").lower()
#     if new_opearation == "n":
#         result = 0
#     elif new_opearation == "end":
#         start = False
#     else :
#         number1 = result

# def add_numbers(a, b):
#     print(a + b) # 7

# result = add_numbers(3, 4) # 7
# print(result) # None

# list_a = [10, 20, 30]
# list_b = list_a
# list_b.append(40)
# print(len(list_a))

# تشير إلى سيارتين بعيدتين عنك: Those are fast cars.

# تشير إلى كتاب واحد قريب في يدك: This is a useful book.

# I am a programmer.

# He / She / It is ready.

# We / You / They are learning Python.
# نحتاجه عند عمل نفي وعند عمل سؤال