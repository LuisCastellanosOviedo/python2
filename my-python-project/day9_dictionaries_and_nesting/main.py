first_dic = {
    "bug": "is a error",
    "Function": "A piece of code",
    "Loop": "some repetitive",
}

# retrieve all elements from the dic
print(first_dic)
print(f"bug values:  {first_dic['bug']}")

# Adding new elements to dictionary
first_dic["Error"] = "A problem in the code"
print(first_dic)

# Create and empty dic
empty_dic = {}

# edit element
first_dic["bug"] = "New value edited !!!!!!"
print(first_dic)

# Loop through a dic
for key in first_dic:
    print(key)
    print(first_dic[key])
