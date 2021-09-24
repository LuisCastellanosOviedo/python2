def greet():
    print("Hello")
    print("how do you do?")
    print("isn't the weather nice today ?")


greet()


def greet_with_name(name):
    print(f"Hello {name}")
    print(f"how do you do {name}?")


greet_with_name("Luis")
greet_with_name(35)

print("More than one parameter ")


def greet_with(name, location):
    print(f"hello {name} what is it like in {location}")


greet_with("tony stark", "new york")
greet_with(location="London", name="Luis")
