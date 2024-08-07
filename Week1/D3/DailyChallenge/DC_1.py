# Ask the user for a number and a length
number = int(input("Please enter a number: "))
length = int(input("Please enter the length of the list: "))

# Create the list of multiples
multiples = [number * i for i in range(1, length + 1)]

# Print the resulting list
print(multiples)
