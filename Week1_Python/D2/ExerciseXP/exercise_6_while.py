#Write a while loop that will continuously ask the user to guess your name, unless the input is equal to your name
my_name = "Manuel"
user_name = ""

while user_name != my_name:
    user_name = input("Please guess my name: ")
    if user_name != my_name:
        print("That's not my name. Please try again.")

print(f"Hello, {my_name}! You've entered the correct name.")
