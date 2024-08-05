list1 = [5, 10, 15, 20, 25, 50, 20]
# looping by the value
# Usually used for using the values in other places
# Building a string, creating a different list etc.

list2 = []

for num in list1:
    list2.append(num * 10)

print(list2)
