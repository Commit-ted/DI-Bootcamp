list1 = [5, 10, 15, 20, 25, 50, 20]
    #    0   1  2   3   4    5  6
# idx = list1.index(20)
# list1[idx] = 200
# print(list1)

# idx = list1.index(20)
# print(idx)
# list1[idx] = 300

# idx = list1.index(20)

while 20 in list1:
    idx = list1.index(20)
    list1[idx] = 200
    
print(list1)

#range(len(list1)) # produces a range from 0 until 7 (len of list1)

for i in range(0, len(list1)):
    if list1[i] == 20:
        list1[i] = 200

print(list1)