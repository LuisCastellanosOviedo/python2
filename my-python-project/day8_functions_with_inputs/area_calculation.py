import math

test_h = int(input("Height of wall: "))
test_w = int(input("Width of wall: "))
coverage = 5


def paint_calc(height, width, cover):
    print(str(math.ceil(height * width / cover)))


paint_calc(height=test_h, width=test_w, cover=coverage)
