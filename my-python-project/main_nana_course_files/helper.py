def days_to_units_ver2(num_of_days, conversion_unit):
    if conversion_unit == "hours":
        return f"{num_of_days} days are {num_of_days * 24} {conversion_unit}"
    elif conversion_unit == "minutes":
        return f"{num_of_days} days are {num_of_days * 24 * 60} {conversion_unit}"
    else:
        return "Unsupported Unit"


def validate_and_execute(days_and_unit_dictionary):
    print(type("it should be a string"))

    try:
        num_of_days_element = days_and_unit_dictionary["days"]
        if num_of_days_element.isdigit():
            user_input_number = int(num_of_days_element)
            if user_input_number > 0:
                print(days_to_units_ver2(user_input_number, days_and_unit_dictionary["unit"]))
            elif user_input_number == 0:
                print("you entered a 0 , please enter a valid positive number ")
            else:
                print("entered a negative value ")
# except: with no value cath everything !
    except ValueError:
        print("please enter a number not text")


user_input_message = "Hey user enter de number of days and conversion unit! :\n"
