# LIST
print("---- LIST ----")
fruits = ["apple", "banana", "cherry"]

print("Original list:", fruits)

fruits.append("orange")
fruits.remove("banana")
fruits[0] = "mango"

print("Updated list:", fruits)


# TUPLE
print("\n---- TUPLE ----")
colors = ("red", "green", "blue")

print("Tuple:", colors)

# Uncomment to show error
# colors[0] = "yellow"


# DICTIONARY
print("\n---- DICTIONARY ----")
student = {
    "name": "Yashika",
    "age": 19
}

print("Original dictionary:", student)

student["age"] = 20
student["grade"] = "A"

print("Updated dictionary:", student)