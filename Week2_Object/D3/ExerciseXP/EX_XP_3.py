#3
# import string
# import random

# def generate_random_string(length=5):
#     letters = string.ascii_letters

#     random_string = ''.join(random.choice(letters) for _ in range(length))
#     return random_string

# print(generate_random_string())

# #4
# import datetime

# def display_current_date():
#     # Get the current date
#     current_date = datetime.datetime.now().date()
    
#     # Print the current date
#     print(f"Today's date is: {current_date}")

# # Example usage
# display_current_date()


#5
# import datetime

# def time_until_new_year():
#     # Get the current date and time
#     now = datetime.datetime.now()
    
#     # Calculate the next January 1st based on the current year
#     next_january_first = datetime.datetime(now.year + 1, 1, 1)
    
#     # Calculate the difference between the current date and January 1st
#     time_left = next_january_first - now
    
#     # Extract days, hours, minutes, and seconds from the time difference
#     days = time_left.days
#     hours, remainder = divmod(time_left.seconds, 3600)
#     minutes, seconds = divmod(remainder, 60)
    
#     # Display the result
#     print(f"The 1st of January is in {days} days, {hours} hours, {minutes} minutes, and {seconds} seconds.")

# # Example usage
# time_until_new_year()


#6
# import datetime

# def calculate_minutes_lived(birthdate_str, date_format="%Y-%m-%d"):
#     # Convert the birthdate string to a datetime object
#     birthdate = datetime.datetime.strptime(birthdate_str, date_format)
    
#     # Get the current date and time
#     now = datetime.datetime.now()
    
#     # Calculate the difference between now and the birthdate
#     time_lived = now - birthdate
    
#     # Convert the difference to minutes
#     minutes_lived = time_lived.total_seconds() / 60
    
#     # Display the result
#     print(f"You have lived for approximately {int(minutes_lived)} minutes.")

# # Example usage
# calculate_minutes_lived("1990-05-15")


#6B

# import datetime

# def calculate_minutes_lived():
#     # Prompt the user to input their birthdate
#     birthdate_str = input("Please enter your birthdate (in YYYY-MM-DD format): ")
    
#     # Define the date format
#     date_format = "%Y-%m-%d"
    
#     try:
#         # Convert the birthdate string to a datetime object
#         birthdate = datetime.datetime.strptime(birthdate_str, date_format)
        
#         # Get the current date and time
#         now = datetime.datetime.now()
        
#         # Calculate the difference between now and the birthdate
#         time_lived = now - birthdate
        
#         # Convert the difference to minutes
#         minutes_lived = time_lived.total_seconds() / 60
        
#         # Display the result
#         print(f"You have lived for approximately {int(minutes_lived)} minutes.")
    
#     except ValueError:
#         print("Invalid date format. Please enter the date in YYYY-MM-DD format.")

# # Example usage
# calculate_minutes_lived()

#7
from faker import Faker

# Initialize the Faker generator
fake = Faker()

# Create an empty list to hold user dictionaries
users = []

def add_fake_user(users_list):
    user = {
        "name": fake.name(),
        "address": fake.address(),
        "language_code": fake.language_code()
    }
    users_list.append(user)

# Example usage
for _ in range(10):  # Generate 10 fake users
    add_fake_user(users)

# Print the list of users
for user in users:
    print(user)
