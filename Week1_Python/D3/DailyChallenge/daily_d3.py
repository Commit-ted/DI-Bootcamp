string = "dodo"

# 1 - Get the word (string)
# 2 - check each letter of the string 
# 3 - create a dictionary
# 4 - put the letter as key 
# 5 - put the index of the letter as value
# 6 - check if the letter is already in the dictionary

output = {}
for i, letter in enumerate(string):
    
    if letter in output:
        output[letter].append(i)
    else:
        output.update({letter : [i]})

print(output)

   
