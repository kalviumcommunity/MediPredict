# Function to add two numbers and return the result
def add_numbers(first_number, second_number):
    return first_number + second_number


# Function to multiply two numbers and return the result
def multiply_numbers(first_number, second_number):
    return first_number * second_number


# Calling functions and storing results for reuse
sum_result = add_numbers(5, 3)
product_result = multiply_numbers(2, 4)

# Combine previous results to demonstrate function reuse
final_result = add_numbers(sum_result, product_result)

# Display results to the user (kept outside functions for clarity)
print("Sum:", sum_result)
print("Product:", product_result)
print("Final Result (Sum + Product):", final_result)