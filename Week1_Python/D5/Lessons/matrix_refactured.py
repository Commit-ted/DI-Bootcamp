# Option1: What we did in class refactured

# Input string
matrix_str = '''7ii
Tsx
h%?
i #
sM 
$a 
#t%
^r!'''

def creating_matrix(matrix_str):
    rows = matrix_str.split('\n')
    matrix = [list(row) for row in rows]
    
    columns = []
    for i in range(len(matrix[0])):
        column = [row[i] for row in matrix]
        columns.append(column)
        
    return columns

def checking_if_letter(letter, decrypted_str):
    if letter.isalpha():
        decrypted_str += letter
    elif len(decrypted_str) > 0 and not letter.isalpha() and decrypted_str[-1] != ' ':
        decrypted_str += ' '
    return decrypted_str

def decrypting_message(matrix):
    decrypted_str = ''
    for column in matrix:
        for letter in column:
            decrypted_str = checking_if_letter(letter, decrypted_str)
    return decrypted_str

# Creating matrix from the input string
matrix = creating_matrix(matrix_str)

# Decrypting the message from the matrix
decrypted_message = decrypting_message(matrix)

# Print the decrypted message
print(decrypted_message)


#Option2: advanced 
import re

MATRIX_STRING = "7i3Tsih%xi #sM $a #t%^r!"
COLUMNS = 3
ROWS = 8

matrix = [char for char in MATRIX_STRING]
matrix = [list(row) for row in zip(*[iter(matrix)]*COLUMNS)]


no_digits_list = list()

for col in range(COLUMNS):
    for row in range(ROWS):
        if not matrix[row][col].isdigit():
            no_digits_list.append(matrix[row][col])

no_digits_string = "".join(no_digits_list)

print(re.sub('[^A-Za-z0-9]+', ' ', no_digits_string))