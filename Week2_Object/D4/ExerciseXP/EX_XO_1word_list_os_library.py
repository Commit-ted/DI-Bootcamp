import random
import os

# Function to read words from the file
def get_words_from_file(file_path):
    with open(file_path, 'r') as file:
        words = file.read().splitlines()
    return words

# Function to generate a random sentence
def get_random_sentence(length, words_list):
    random_words = random.sample(words_list, length)
    sentence = ' '.join(random_words).lower()
    return sentence

# Main function to run the program
def main():
    print("This program generates a random sentence of a specified length.")
    
    try:
        length = int(input("How many words should the sentence have? (Enter a number between 2 and 20): "))
        
        if 2 <= length <= 20:
            # Use os.path to create a file path
            base_dir = os.path.dirname(__file__)  # Gets the directory where the script is located
            file_name = 'word_list.rtf'
            file_path = os.path.join(base_dir, file_name)  # Constructs the full path to the file
            
            if os.path.exists(file_path):  # Check if the file exists
                words_list = get_words_from_file(file_path)
                sentence = get_random_sentence(length, words_list)
                print(f"Generated Sentence: {sentence}")
            else:
                print(f"Error: The file '{file_name}' does not exist in the directory '{base_dir}'.")
        else:
            print("Error: Please enter a number between 2 and 20.")
    except ValueError:
        print("Error: Invalid input. Please enter a valid integer.")

# Run the main function
if __name__ == "__main__":
    main()
