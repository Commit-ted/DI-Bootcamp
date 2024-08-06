# Ask the user for a string and delete the consecutive duplicates
user_string = input("Please enter a string: ")

# Initialize an empty string to store the result
result_string = ""
i = 0

# Check if the string is not empty
if len(user_string) > 0:
    current_character = user_string[0]
    result_string += current_character

# Iterate through the user string starting from the second character
while i < len(user_string):
    if user_string[i] != current_character:
        current_character = user_string[i]
        result_string += current_character
    i += 1

# Print the resulting string
print("Resulting string:", result_string)






