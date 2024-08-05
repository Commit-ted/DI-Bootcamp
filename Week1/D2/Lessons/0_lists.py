# List (array)
# Can hold any type of values
# To access the values inside we use indexing (0-first value inside the list...)
# Mutable - Can be changed

# access, modify, delete

a_list = []  # a list

print(type(a_list))

a_list = [1, 2, 3, 4, 5, 6, 7]
# 0  1  2  3  4  5  6  len(a_list)
print(a_list)

# ACCESS
# use indexing

first_value = a_list[0]
print(first_value)

last_value = a_list[-1]
print(last_value)

# Slicing
sub_list = a_list[0:3]
# starting point - 0 - included
# end point - 3 - excluded
# We slice starting from index 0 UNTIL 4

print(sub_list) # [1, 2, 3]

list_size = len(a_list)
print(list_size)

# len(a_list)//2 - middle index of the list
sublist_b = a_list[len(a_list) // 2 :]

print(sublist_b)

# to run until the end - just leave it blank after the ':' sign
# a_list[3:] - starts at index 3 and goes up until the end


# MODIFING

b_list = ["a", "c", 2, 10]
#  0   1   2   3

b_list[2] = 20

print(b_list)

b_list[0] = b_list[0].capitalize()

print(b_list)

b_sublist = b_list[:2]

print(b_sublist)

b_sublist[0] = "B"

print(b_sublist)
print(b_list)


# DELETION

c_list = [1, 2, 3, 3] # [, <-2, <-3, <-3]

c_list.remove(3) # removes the first occurence of 3

print(c_list)

deleted_value = c_list.pop() # removes the last element

print(c_list)
print(deleted_value)

c_list.pop(1) # using index to remove
print(c_list)

