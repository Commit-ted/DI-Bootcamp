import datetime as dt
from decimal import Decimal
from random import randint, choice
import custom_module

# Get the current date
current_date = dt.date.today()

# Get the current time
current_time = dt.datetime.now().time()

# Extract the current year as an integer
current_year = current_date.year  # This ensures current_year is an int

# Define the range for the random year based on the current year
start_year = current_year  # Use the current year as the start year
end_year = 4537  # Define the end year

# Generate a random target year for time travel within the specified range
target_year = randint(start_year, end_year)

# Display the random target year generated
print(f"Random Target Year for Time Travel: {target_year}")

# Create a base cost as a Decimal object
base_cost = Decimal('700.50')

# Calculate the absolute year difference
year_difference = abs(target_year - current_year)

# Determine a cost multiplier based on the year difference
cost_multiplier = Decimal('1.05') ** year_difference  # Example multiplier rate of 5% per year

# Calculate the final cost
final_cost = base_cost * cost_multiplier

# Ensure the final cost is formatted to two decimal places
formatted_cost = f"{final_cost:.2f}"

# Create a list of possible destinations for time travel
destinations = ['Ancient Egypt', 'Medieval Europe', 'The Wild West', 'Future Mars Colony', 'The Roaring Twenties']

# Randomly select a destination from the list
selected_destination = choice(destinations)

# Generate the time travel message using the custom module
time_travel_message = custom_module.generate_time_travel_message(target_year, selected_destination, formatted_cost)

# Print the generated time travel message
print(time_travel_message)
