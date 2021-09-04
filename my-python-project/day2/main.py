#Data types

#strings

print(f"Hello index {'Hello'[1]}")

#Integer

123

print(f"integer add 123+456 = {123+456}")

#Float

3.1416

print(f" float example : {3.14165}")
print(f"float using under score 345_455.678 : {345_455.678}")

#Boolean

print(True)
print(False)


#Functions
"""
num_char = len(input("What is your name ???"))
print(f" num to str : {str(num_char)}")
print(f"Your nama has {num_char} characters.")
"""

print(70 + float("100.5"))

print("######### ######### ######### ######### ######### ######### ")
"""
two_digit_number = input(" type 2 digit number = ")
print(type(two_digit_number))
print(f" add each digit {two_digit_number[0]} + {two_digit_number[1]} ="
      f" {int(two_digit_number[0])+int(two_digit_number[1])}")
"""
print("######### ######### ######### ######### ######### ######### ")

print(f"divitions always return float {type(6/3)}")
print(f" example power using ** {2**3}")

print("######### ######### ######### ######### ######### ######### ")
print(" gerarquias ")
print("PEMDAS")
print("**")
print("* / ")
print(" + - ")

print(3 * 3 + 3 / 3 -3)

print("######### ######### ######### ######### ######### ######### ")

height = input("enter your height in m:")
weight = input("enter your weight in kg:")

bmi = int(weight) / float(height) ** 2
bmi_as_int = int(bmi)
print(bmi_as_int)

print("######### ######### ######### ######### ######### ######### ")
print("ROUND numbers")
print(round(8/3, 2))
print(round(8//3))








