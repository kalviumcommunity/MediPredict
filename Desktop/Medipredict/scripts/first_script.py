# Numeric Data Types
a = 10
b = 2.5

print("Integer value:", a)
print("Float value:", b)

print("Addition:", a + b)
print("Division:", a / b)


# String Data Types
name = "Yashika"
greeting = "Hello"

print(greeting + " " + name)


# Mixing Types (Important)
age = 20

# Wrong way (will error)
# print("Age is " + age)

# Correct way
print("Age is " + str(age))


# Type Conversion
num_str = "50"
num_int = int(num_str)

print("Converted number:", num_int + 10)


# Type Checking
print(type(a))
print(type(b))
print(type(name))
print(type(num_str))


# Bonus (to impress)
print(f"My name is {name} and I am {age} years old")