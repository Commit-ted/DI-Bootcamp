# Ask the user for a number and a length
number = int(input("Please enter a number: "))
length = int(input("Please enter the desired length of the list: "))

# Initialize an empty list to store the multiples
multiples_list = []

# Generate the list of multiples
for i in range(1, length + 1):
    multiples_list.append(number * i)

# Print the resulting list
print(multiples_list)
