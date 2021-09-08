import random
from my_module import pi

random_integer = random.randint(1, 10)
print(random_integer)
print(pi)

random_float = random.random()
print(random_float)
print(round((random_float * 5), 2))

random_decimal = random.randrange(0, 5)
print(random_decimal)
