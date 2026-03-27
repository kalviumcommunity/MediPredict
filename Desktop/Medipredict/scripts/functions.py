# 1. Simple function
def greet():
    print("Hello! Welcome to Python Functions")

# Calling the function
greet()


print("-----")


# 2. Function with parameters
def greet_user(name):
    print("Hello", name)

greet_user("Yashuuu")


print("-----")


# 3. Function with return value
def add_numbers(a, b):
    return a + b

result = add_numbers(5, 3)
print("Sum:", result)


print("-----")


# 4. Function using condition
def check_even_odd(number):
    if number % 2 == 0:
        return "Even"
    else:
        return "Odd"

print("Number is:", check_even_odd(4))