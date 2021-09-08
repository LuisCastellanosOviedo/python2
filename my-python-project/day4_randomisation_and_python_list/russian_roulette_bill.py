import random


names_string = input("Give me everybody's names, separated by a comma.")
list_of_people = names_string.split(",")
print(f"{list_of_people[random.randint(0,len(list_of_people))]} should pay the bill MUAHAHAHAHAHA")