from random import randint

EASY_LEVEL_TURNS = 10
HARD_LEVEL_TURNS = 5


def check_answer(guess, answer):
    if guess > answer:
        print("too hight")
    elif guess < answer:
        print("too low")
    else:
        print("you got it ! ")


def set_difficulty():
    level = input("Choose dificulty:  ")
    if level == "easy":
        return EASY_LEVEL_TURNS
    else:
        return HARD_LEVEL_TURNS


answer = randint(1, 100)
print("guess the number between 1 and 100")
turns = 0
int(input("Make a guess"))
