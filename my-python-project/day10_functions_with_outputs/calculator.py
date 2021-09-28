from art import logo

print(logo)


def add(n1, n2):
    return n1 + n2


def subtract(n1, n2):
    return n1 - n2


def multiply(n1, n2):
    return n1 * n2


def divide(n1, n2):
    return n1 / n2


print(type(add))
operators = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide,
}

num1 = float(input("first number: "))
num2 = float(input("second number: "))

for symbol in operators:
    print(symbol)

operation_symbol = input("Pick an operation: ")
print(f" the result {operators[operation_symbol](num1, num2)}")
