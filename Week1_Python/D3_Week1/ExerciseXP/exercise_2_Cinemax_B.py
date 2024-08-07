#Bonus
family = {}

while True:
    name = input("Please enter a family member's name (or type 'done' to finish): ").strip()
    if name.lower() == 'done':
        break
    age = int(input(f"Please enter the age of {name}: ").strip())
    try:
        family[name] = age
    except ValueError:
        print("Invalid age. Please enter a numeric value.")

total_cost = 0
individual_cost = {}

for name, age in family.items():
    if age < 3:
        cost = 0
    elif 3 <= age <= 12:
        cost = 10
    else:
        cost = 15
    individual_cost[name] = cost
    total_cost += cost

# Print the cost for each family member
for name, cost in individual_cost.items():
    print(f"{name.capitalize()} has to pay: ${cost}")

# Print the total cost for the family
print(f"\nTotal cost for the family's movie tickets: ${total_cost}") 
