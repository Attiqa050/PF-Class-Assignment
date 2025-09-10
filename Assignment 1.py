
# Task 1: User enters 10 numbers (5 in each list), then merge and sort

print("Enter 5 numbers for List 1:")
a = int(input("Number 1: "))
b = int(input("Number 2: "))
c = int(input("Number 3: "))
d = int(input("Number 4: "))
e = int(input("Number 5: "))
list1 = [a, b, c, d, e]
print("Enter 5 numbers for List 2:")
f = int(input("Number 6: "))
g = int(input("Number 7: "))
h = int(input("Number 8: "))
i = int(input("Number 9: "))
j = int(input("Number 10: "))

list2 = [f, g, h, i, j]

merged = list1 + list2
merged.sort()

print("Merged and sorted list is:", merged)

# Task 2: Find smallest and largest number
print("Smallest number is:", min(merged))
print("Largest number is:", max(merged))

# Task 3: Birthday dictionary

birthdays = {
    "Albert Einstein": "03/14/1879",
    "Benjamin Franklin": "01/17/1706",
    "Ada Lovelace": "12/10/1815"
}

print("We know the birthdays of:")
print("Albert Einstein, Benjamin Franklin, Ada Lovelace")

name = input("Enter a name: ")

if name in birthdays:
    print(name, "'s birthday is", birthdays[name])
else:
    print("Sorry, not in dictionary.")


# Task 4: Extract some keys from dictionary

dict = {
    "name": "Kelly",
    "age": 25,
    "salary": 8000,
    "city": "New York"
}

new_dict = {
    "name": dict["name"],
    "salary": dict["salary"]
}

print("New dictionary is:", new_dict)
