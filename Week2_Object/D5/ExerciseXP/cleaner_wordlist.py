# Define the input and output file paths
input_file_path = '/Users/manuel/Desktop/DI-Bootcamp/Week2_Object/D5/ExerciseXP/wordlist.txt'
output_file_path = '/Users/manuel/Desktop/DI-Bootcamp/Week2_Object/D5/ExerciseXP/cleaned_wordlist.txt'

# Open the input file and read its contents
with open(input_file_path, 'r') as file:
    content = file.read()

# Remove unwanted characters
cleaned_content = content.replace('\\', '').replace("'", '').replace('{', '').replace('}', '')

# Split the cleaned content into lines
cleaned_lines = cleaned_content.splitlines()

# Write the cleaned content to the output file
with open(output_file_path, 'w') as file:
    for line in cleaned_lines:
        if line.strip():  # Avoid writing empty lines
            file.write(line.strip() + '\n')

print("Wordlist cleaned and saved to:", output_file_path)
