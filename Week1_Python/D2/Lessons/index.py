#find the value 20 in the list, and if it is present, replace it with 200
list1 = [5, 10, 15, 20, 25, 50, 20]

change_20 = list1.index(20)

list1[change_20] = 200

print(list1)
print(change_20)