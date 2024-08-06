#Convert the two following lists, into dictionaries.
#Hint: Use the zip method

#Expected output:
#{'Ten': 10, 'Twenty': 20, 'Thirty': 30}

keys = ['Ten', 'Twenty', 'Thirty']
values = [10, 20, 30]
#extra_value = ["$", "@", "*"]

dict_a = keys
dict_b = values

result_dict = dict(zip(keys,values))
print(result_dict)