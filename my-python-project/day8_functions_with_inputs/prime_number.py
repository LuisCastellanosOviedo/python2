def prime_checker(number):
    for num in range(1, number + 1):
        if num != 1 and num != number and number % num == 0:
            return "Not prime"
    return "Prime"


while True:
    n = int(input("Check this number: "))
    print(prime_checker(number=n))
