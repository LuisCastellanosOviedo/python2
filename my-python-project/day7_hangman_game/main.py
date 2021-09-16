import random

word_list = ["hook", "baboon", "camel"]

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

guess = input("Guess a letter: ").lower()

for position in range(len(chosen_word)):
    letter = chosen_word[position]
    if letter == guess:
        display[position] = letter
        print("Right")
    else:
        print("Wrong bitch ! ")

print(display)
