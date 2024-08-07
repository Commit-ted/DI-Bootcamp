#Calcullations from a list
family = {"rick": 43, 'beth': 13, 'morty': 5, 'summer': 8}

total_cost = 0
individual_cost = {}

for name, age in family.items():
    if age < 3:
        cost = 0
    elif 3<= age >=12:
        cost = 10
    else:
        cost = 15
    individual_cost[name] = cost
    total_cost += cost

for name, cost in individual_cost.items():
    print(f"{name.capitalize()} has to pay: ${cost}")
print(f"\n Total cost for the family's movie tickets: ${total_cost}")
