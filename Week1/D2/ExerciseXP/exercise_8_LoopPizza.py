# Initialize an empty list to store pizza toppings
toppings = []

base_price = 10
topping_price = 2.5

# Loop to ask the user for pizza toppings
while True:
    topping = input("Enter a pizza topping (or type 'quit' to finish): ").strip().lower()
    if topping == "quit":
        break
    else:
        toppings.append(topping)
        print(f"Adding {topping} to your pizza: ")

# calculate price
total_price = base_price + (topping_price * len(toppings))
print("\n Toppings on your Pizza: ")
for topping in toppings:
    print(f"- {topping}")

print(f"\nTotal price: ${total_price:.2f}")