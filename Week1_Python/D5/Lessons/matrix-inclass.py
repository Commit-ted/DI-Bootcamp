matrix_str = '''7ii
Tsx
h%?
i #
sM 
$a 
#t%
^r!'''

# [[7,T,h],[i,s,$],#,^]

# matrix = []

# for i in range(len(matrix_str)):
#     sublist = [matrix_str[i:i+3]]
#     if '\n' in sublist:
#         sublist.pop('\n')
#     matrix.append(sublist)

#split(\n)

rows = matrix_str.split('\n')
rows_clean = rows
print(rows)

# for row in rows:
#     matrix.append(list(row))

#list comprehension
matrix = [list(row) for row in rows]

print(matrix)

column0 = []
column1 = []
column2 = []

for row in matrix:
    column0.append(row[0])
    column1.append(row[1])
    column2.append(row[2])

matrix = []
matrix.append(column0)
matrix.append(column1)
matrix.append(column2)

print(matrix)

decrypted_str = ''
for column in matrix:
    for i, letter in enumerate(column):
        if letter.isalpha():
            decrypted_str += letter
        elif len(decrypted_str) > 0 and not letter.isalpha() and decrypted_str[-1] != ' ':
            decrypted_str += ' '

print(decrypted_str)

    

