# # =============== Day 11 ===============
# import random
# cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
# restart = True

# def random_cards():
#     r1 = [random.choice(cards),random.choice(cards)]
#     return r1

# def calcscore(s1):
#     score = sum(s1)
#     return score

# def checkgame(usrscore, compscore):
#     if usrscore > 21 :
#         print("You went over. You lose 😭")
#     elif compscore > 21 :
#         print("Computer went over. You win! 😎")
#     elif usrscore == compscore:
#         print("draw")
#     elif usrscore < compscore :
#         print("You went over. You lose 😭")
#     else :
#         print("You win")

# def playgame():
#     anothergame = True
#     user_random_cards = random_cards()
#     computer_random_cards = random_cards()

#     userscore = calcscore(user_random_cards)
#     compscore = calcscore(computer_random_cards)
#     print(f"Your cards: {user_random_cards}, current userscore: {userscore}")
#     print(f"Computer's first card: {computer_random_cards[0]}")
#     if userscore >= 21:
#             checkgame(userscore, compscore)
#             anothergame = False
#     while anothergame:
#         if userscore >= 21:
#             checkgame(userscore, compscore)
#             anothergame = False
#             break
#         another_card = input("Type 'y' to get another card, type 'n' to pass: ").lower()
#         if another_card == "y":
#             user_random_cards.append(random.choice(cards))
#             userscore += user_random_cards[-1]
#             print(f"Your cards: {user_random_cards}, current userscore: {userscore}")
#             print(f"Computer's final card: {computer_random_cards[-1]}, final score: {compscore}")
            
#         elif another_card == "n" :
#             print(f"Your cards: {user_random_cards}, current userscore: {userscore}")
#             print(f"Computer's final card: {computer_random_cards[-1]}, final score: {compscore}")
            
#             break
#         else:
#                 print("Please type 'y' or 'n'.")

# while restart :
#     replay = input("Do you want to play a game of Blackjack? Type 'y' or 'n': ").lower()
#     if replay == "y":
#         playgame() 
#     elif replay == "n":
#         print("Good Bye 👋")
#         break
#     else:
#         print("Please type 'y' or 'n'.")