import random
from replit import clear
from hangman_art import logo, stages
from hangman_words import word_list

print(logo)

chosen_word = random.choice(word_list)
print(print(f" here is the word {chosen_word}"))

display = []
for _ in chosen_word:
    display += "_"
print(display)

display = []
for _ in range(len(chosen_word)):
    display += "_"
print(display)

end_of_game = False

count = 5
while not end_of_game:

    guess = input("Guess a letter: ").lower()
    clear()

    letterPresent = False
    for position in range(len(chosen_word)):
        letter = chosen_word[position]
        if letter == guess:
            display[position] = letter
            letterPresent = True

    if not letterPresent:
        print(stages[count])
        count -= 1

    print(display)
    if count < 0:
        print("You !!! looserrrr ")
        end_of_game = True

    if "_" not in display:
        end_of_game = True
        print("You Win ! ")
