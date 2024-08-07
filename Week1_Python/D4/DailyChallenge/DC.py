matrix = [
    ['7', 'i', 'i'],
    ['T', 's', 'x'],
    ['h', '%', '?'],
    ['i', ' ', '#'],
    ['s', 'M', ' '],
    ['$', 'a', ' '],
    ['#', 't', '%'],
    ['^', 'r', '!']
]

def decode_matrix(matrix):
    rows = len(matrix)
    cols = len(matrix[0])
    decoded_message = []
    
    for col in range(cols):
        for row in range(rows):
            char = matrix[row][col]
            if char.isalpha():
                decoded_message.append(char)
            else:
                # Add a space only if the last added character isn't a space
                if decoded_message and decoded_message[-1] != ' ':
                    decoded_message.append(' ')
    
    # Convert list to string and remove leading/trailing spaces
    return ''.join(decoded_message).strip()

# Decode the matrix
decoded_message = decode_matrix(matrix)
print("Decoded message:", decoded_message)
