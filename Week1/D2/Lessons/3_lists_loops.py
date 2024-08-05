list1 = [5, 10, 15, 20, 25, 50, 20]
#   [0, 1,   2,  3,  4,  5,  6]
# looping by the index
# we would like to do so, mainly to have access to the memory
# for reasons: changing the values inside the original list etc.

# we use range() function to produce the index range
numbers = range(0, 10)
numbers = list(range(0, len(list1)))
print(numbers)

for i in range(0, len(list1)):
    list1[i] = list1[i] * 10 # *=

print(list1)
