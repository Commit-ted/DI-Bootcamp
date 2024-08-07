a_list = [1, 2, 3, 4, 5, 6, 7]

# ACCESS
# a_list[0] <- first value
# a_list[1] <- last value
# a_list[-2] <- second last value

# a_list[0:3] <- [1, 2, 3]
# a_list[:3] <-  [1, 2, 3]
# a_list[4:] <-  [5, 6, 7]
# a_list[-3:] <- [5, 6, 7]

# print(a_list[-1::-1]) # reversing the list
# a_list.reverse()


# ADD
a_list = [1, 2, 3, 4, 5, 6, 7]

a_list.append(8)  # add to the end of the list
a_list.append(9)
print(a_list)

a_list += [10, 11, 12]  # adding 2 lists together
print(a_list)

a_list.append(["ASDFASFSAF", 1, 2,])
print(a_list)

del a_list[:3]
print(a_list)