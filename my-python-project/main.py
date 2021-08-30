#easiest way !
#import helper

from helper import validate_and_execute, user_input_message


COMMA = ","
print(1)
print("2 is a number")
print('2 is a greate number using single cuote')
print(22.4)


print(20 * 24 * 60)
print(" FORMAT ********************** ********************** ********************** *********************")

print("20 days are " + str(20 * 24 * 60) + " minutes")
print(f"20 days are {20 * 24 * 60} minutes using format style ")


print(" VARIABLES  ********************** ********************** ********************** *********************")
calculation_to_units = 24 * 60 * 60
name_of_unit = "seconds"

print(f"20 days are {20 * calculation_to_units} {name_of_unit} using format style ")
print(f"35 days are {35 * calculation_to_units} {name_of_unit} using format style ")
print(f"50 days are {50 * calculation_to_units} {name_of_unit} using format style ")


print(" FUNCTIONS  ********************** ********************** ********************** *********************")

calculation_to_units = 24 * 60 * 60
name_of_unit = "seconds"


def days_to_units():
    print(f"1 days are {1 * calculation_to_units} {name_of_unit} using format style ")
    print("ALL good ! inside function !!!!")


days_to_units()

print(f"20 days are {20 * calculation_to_units} {name_of_unit} using format style ")
print(f"35 days are {35 * calculation_to_units} {name_of_unit} using format style ")
print(f"50 days are {50 * calculation_to_units} {name_of_unit} using format style ")


print(" FUNCTION PARAMETERS ********************** ********************** ********************** *********************")


def days_to_units_parameters(num_of_days,custom_message):
    print(f"{num_of_days} days are {num_of_days * calculation_to_units} {name_of_unit} using format style ")
    print(f"FUCNTION WITH PARAMETERS AND A CUSTOM MESSAGE {custom_message}")


def scope_check(num_of_days):
    my_variable = "variable inside the function"
    print(name_of_unit)
    print(num_of_days)
    print(my_variable)


days_to_units_parameters(20, " awesome ! ")
days_to_units_parameters(35, " awesome ! ")
days_to_units_parameters(50, " awesome ! ")

scope_check(2)

"""
print(" USER INPUT  ********************** ********************** ********************** *********************")

user_input = input(" Enter number of days ! \n")
print(f"value entered {user_input}")


print(" FUNCTIONS WITH RETURNS  ********************** ********************** ********************** **************")


def days_to_units_return(num_days):
    return f"This are the days returned {num_days}"


print(days_to_units_return(35))

value = input("add new value")
int(value)
"""
print(" CONDITIONALS  ********************** ********************** ********************** **************")


def print_value(value_to_print):
    condition_check = int(value_to_print) > 10
    print(type(condition_check))
    return f"Value given {value_to_print}"


to_print = ""
while to_print != "exit":
    """
    to_print = input("Hey user enter de number of days and conversion unit! :")
    print(type(to_print.split(COMMA)))
    print(to_print.split(COMMA))
    print(set(to_print.split(COMMA)))
    print(f"check set type {type(set(to_print.split(COMMA)))}")
   for num_of_days_element in set(to_print.split(COMMA)):
        validate_and_execute()
    """

    to_print = input(user_input_message)
    days_and_unit = to_print.split(":")
    print(days_and_unit)
    # Dictionary sintax
    # {"days":20, "unit","hours"}
    days_and_unit_dictionary = {"days": days_and_unit[0], "unit": days_and_unit[1]}
    print(days_and_unit_dictionary)
    print(type(days_and_unit_dictionary))

    """ using only import
    helper.validate_and_execute(days_and_unit_dictionary)
    """

    validate_and_execute(days_and_unit_dictionary)










