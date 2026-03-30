# Function 1: Add two numbers
def add_numbers(a, b):
    return a + b


# Function 2: Multiply two numbers
def multiply_numbers(x, y):
    return x * y


# Calling functions and storing results
sum_result = add_numbers(5, 3)
product_result = multiply_numbers(2, 4)

# Using returned values again
final_result = add_numbers(sum_result, product_result)

# Printing results (ONLY outside functions)
print("Sum:", sum_result)
print("Product:", product_result)
print("Final Result (Sum + Product):", final_result)