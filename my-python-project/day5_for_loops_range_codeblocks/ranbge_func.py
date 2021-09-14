# increase by 1
for number in range(1, 10):
    print(number)

print("increase by 3")
# increase by 3
for number in range(1, 10, 3):
    print(number)

print("gauss example ")
total = 0
for n in range(1, 101):
    total += n

print(total)

print(" add all even number form 1 to 100")
total = 0
for n in range(2, 101, 2):
    total += n

print(f"add even numbers {total}")
