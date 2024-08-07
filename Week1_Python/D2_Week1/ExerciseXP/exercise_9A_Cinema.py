# Initialize total cost
total_cost = 0

# Ask the family for the ages of each person who wants a ticket
while True:
    age_input = input("Enter the age of a family member (or type 'done' to finish): ").strip()
    if age_input.lower() == 'done':
        break
    try:
        age = int(age_input)
        if age < 3:
            ticket_price = 0
        elif 3 <= age <= 12:
            ticket_price = 10
        else:
            ticket_price = 15
        total_cost += ticket_price
    except ValueError:
        print("Please enter a valid age or 'done' to finish.")

# Print the total cost
print(f"\nTotal cost of all the family's tickets: ${total_cost:.2f}")
