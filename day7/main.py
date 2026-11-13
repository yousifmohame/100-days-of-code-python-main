# ============ Day 7 ===============
import random
import hangman_art
import hangman_words

random_word = random.choice(hangman_words.word_list)

print(random_word)

lives = 6
game_over = False
correct_letter = []

print(hangman_art.logo3)

while not game_over :
    guess = input("guess the letter \n").lower()
    display_blank = ""

    for word in random_word :
        if guess == word :
            display_blank += guess
            correct_letter.append(guess)
        elif word in correct_letter:
            display_blank += word
        else :
            display_blank += "_"
    if guess not in random_word:
        lives -= 1
        print(hangman_art.stages[lives])

    print(display_blank)
    print(f"lives: {lives}")
    if lives == 0 :
        game_over = True
        print("you lost")
    if "_" not in display_blank :
        game_over = True
        print("you win")
        print(hangman_art.logo2)

