print("fizz buzz")

for n in range(1, 101):
    fizz_buzz = str(n)
    if n % 3 == 0:
        fizz_buzz = "Fizz"
    if n % 5 == 0:
        fizz_buzz += "Buzz"
    print(fizz_buzz)
