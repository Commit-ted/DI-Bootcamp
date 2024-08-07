# List of sandwich orders
sandwich_orders = [
    "Tuna sandwich",
    "Pastrami sandwich",
    "Avocado sandwich",
    "Pastrami sandwich",
    "Egg sandwich",
    "Chicken sandwich",
    "Pastrami sandwich"
]

# Remove all occurrences of "Pastrami sandwich"
while "Pastrami sandwich" in sandwich_orders:
    sandwich_orders.remove("Pastrami sandwich")

# Create an empty list to hold finished sandwiches
finished_sandwiches = []

# Prepare the orders of the clients
while sandwich_orders:
    current_sandwich = sandwich_orders.pop(0)
    print(f"I made your {current_sandwich.lower()}")
    finished_sandwiches.append(current_sandwich)

# Print a message listing each sandwich that was made
print("\nAll sandwiches have been made:")
for sandwich in finished_sandwiches:
    print(f"I made your {sandwich.lower()}")
