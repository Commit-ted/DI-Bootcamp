# Ask the user for a string
user_string = input("Please enter a string that is exactly 10 characters long: ")

# Check the length of the string and print appropriate messages
if len(user_string) < 10:
    print("String not long enough")
elif len(user_string) > 10:
    print("String too long")
else:
    print("Perfect string")

    # Print the first and last characters
    print(f"First character: {user_string[0]}")
    print(f"Last character: {user_string[-1]}")
    
    # Construct the string character by character using a for loop
    constructed_string = ""
    for char in user_string:
        constructed_string += char
        print(constructed_string)
