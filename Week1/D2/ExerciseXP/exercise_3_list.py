# Initial list
basket = ["Banana", "Apples", "Oranges", "Blueberries"]
print(basket)

basket.remove("Banana")

basket.remove("Blueberries")

basket.append("Kiwi")

basket.insert(0, "Apples")

print(basket)

count_apples = basket.count("Apples")

print(count_apples)
print(f"the number of apples is: {count_apples}")

# Empty the basket
basket.clear()
print(basket)