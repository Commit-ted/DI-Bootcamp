# Ask the user for a string
user_string = input("Please enter a string: ")

# Initialize an empty string to store the result
result_string = ""

# Iterate through the user string
for i in range(len(user_string)):
    # Add the current character to the result if it's the first character or different from the previous one
    if i == 0 or user_string[i] != user_string[i - 1]:
        result_string += user_string[i]

# Print the resulting string
print("Resulting string:", result_string)
