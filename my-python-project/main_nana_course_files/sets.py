my_set = {"January","February","March"}

for elem in my_set:
    print(f" set value : {elem}")


my_set.add("April")
print(my_set)

print("test remove func")
my_set.remove("January")
print(f" remove January {my_set}")
