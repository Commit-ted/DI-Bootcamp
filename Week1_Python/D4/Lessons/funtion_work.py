def calculate_sum_and_difference():
    # Ask the user for two numbers
    num1 = float(input("Please enter the first number: "))
    num2 = float(input("Please enter the second number: "))
    # Calculate the sum and difference
    sum_result = num1 + num2
    difference_result = num1 - num2
    # Print the results
    print(f"The sum of {num1} and {num2} is: {sum_result}")
    print(f"The difference when {num2} is subtracted from {num1} is: {difference_result}")

# Call the function
calculate_sum_and_difference()



# Method basic
b = 7
a = 4
def calculation(a, b):
    add = a + b
    sub = a - b
    return add, sub
# Call the function and store the result in a tuple
res = calculation(a, b) # This will return a tuple (add, sub)
# Unpack the returned tuple into two variables
add, sub = calculation(a, b) # This will unpack the tuple into add and sub

# Print the results
print(f"Result tuple: {res}")
print(f"Addition result: {add}")
print(f"Subtraction result: {sub}")
