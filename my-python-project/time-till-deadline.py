from _datetime import datetime

user_input =input("enter your goal with a deadline separated by colon \n")
input_list = user_input.split(":")

goal = input_list[0]
deadline = input_list[1]

print(input_list)

deadline_date = datetime.strptime(deadline, "%d.%m.%Y")
today_date = datetime.today()

print(deadline_date)
print(type(deadline_date))
print(today_date)
# calculate how many days form now till the deadline

print(f"The time left to get the goal es {(deadline_date - today_date).days} days.")
print(f"The time left to get the goal es {int((deadline_date - today_date).total_seconds())} hours.")






