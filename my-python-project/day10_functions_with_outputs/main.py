def my_function():
    return 3 * 2


multiply = my_function()
print(multiply)


def format_name(name, last_name):
    if name == "":
        return
    else:
        return f"{name} {last_name}".title()


print(format_name("tony", "stark"))
print(type(format_name("", "")))
