import random


names_string = input("Give me everybody's names, separated by a comma.")
list_of_people = names_string.split(",")
print(f"{list_of_people[random.randint(0,len(list_of_people)-1)]} should pay the bill MUAHAHAHAHAHA")


print("or easy way ")
print(random.choice(list_of_people))