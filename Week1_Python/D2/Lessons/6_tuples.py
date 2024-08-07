# Tuples are like lists, but they cannot be modified after created
# Tuples are READ-ONLY lists
# Usually they store some sensitive and unchanging information

a_tuple = (1, 2, 3, 4, 5)

# ACCESS - same as with list
first_value = a_tuple[0]
last_value = a_tuple[-1]

for val in a_tuple:
    print(val)

# a_tuple[0] = 10 # Leads to an error

sub_tuple = a_tuple[0:3]
print(sub_tuple)

b_tuple = ("Yossi", "Tel Aviv", 32)