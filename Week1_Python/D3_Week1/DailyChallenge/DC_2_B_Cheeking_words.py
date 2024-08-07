# Approach 1: Using a For Loop with enumerate
word = input("Please enter the word: ")
result_string = ""

for i, char in enumerate(word):
    if i == 0 or char != word[i - 1]:
        result_string += char

print("Resulting string:", result_string)
