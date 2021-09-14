students_heights = input(" Input a list of student heights:").split()
summ = 0
for n in range(0, len(students_heights)):
    students_heights[n] = int(students_heights[n])
    summ += students_heights[n]

print(students_heights)
print(summ)
print(round(summ / len(students_heights)))

print("ORRRRR")
total = sum(students_heights)
print(total)

