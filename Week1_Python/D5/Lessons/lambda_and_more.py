from functools import reduce

#the not do efective way
fruits = ['Apple', 'Banana', 'Pear', 'Apricot']

# fruits_upper = []
# for fruit in fruits:
#     fruits_upper.append(fruit.upper())

# print(fruits_apper)

#regular function
def upper_string(s):
    return s.upper()

#using map
fruits_upper = list(map(upper_string,fruits))
# print(fruits_upper)

#using lambda function
fruits_upper = list(map(lambda fruit : fruit.upper(),fruits))
print(fruits_upper)

#lambda example2

numbers = [1,4,3,2,5,6]

#"regular way"
for i, n in enumerate(numbers):
    numbers[i] = n ** 2

print(numbers)
#with lambda

numbers_topower = [1,4,3,2,5,6]
powered_nums = list(map(lambda n : n **2, numbers_topower))
print(powered_nums)

powered = lambda n,power : n ** power
print(powered(4,5))

#filter

def starts_withA(s):
    return s[0] == 'A'

starts_A = list(filter(starts_withA, fruits))
print(starts_A)


def sum_numbers(a,b):
    return a*b

my_list = [1,3,5,6,19]

reduced_list = reduce(sum_numbers,my_list)
print(reduced_list)





