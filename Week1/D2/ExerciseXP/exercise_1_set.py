#Create a set
my_fav_numbers = {3, 7, 14, 21}
print(my_fav_numbers)

# Add two new numbers to the set
my_fav_numbers.update([42, 56])
print(my_fav_numbers)

# Remove the last number (since sets are unordered, we'll convert to a list to remove the last element)
my_fav_numbers = set(list(my_fav_numbers)[:-1])
print(my_fav_numbers)

# Create a set with your friend's favorite numbers
friend_fav_numbers = {5, 10, 15, 20}

# Concatenate both sets to a new variable
our_fav_numbers = my_fav_numbers.union(friend_fav_numbers)

# Print the results
print("My favorite numbers:", my_fav_numbers)
print("Friend's favorite numbers:", friend_fav_numbers)
print("Our favorite numbers:", our_fav_numbers)