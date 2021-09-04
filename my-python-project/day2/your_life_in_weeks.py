age = input("What is your current age ? ")
age_as_int = int(age)
years_remaining = 90 - age_as_int
days_remaing = years_remaining * 365
weeks_remaining = years_remaining * 52
months_remaining = years_remaining * 12

message = f" months {months_remaining} , years {years_remaining} weeks {weeks_remaining} days {days_remaing}"
print(message)