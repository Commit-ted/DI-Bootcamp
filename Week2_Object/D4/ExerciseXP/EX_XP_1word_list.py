import random

def get_words_from_file(file_path):
    with open(file_path, 'r') as file:
        words = file.read().splitlines()
    return words

def get_random_sentence(length, words_list):
    random_words = random.sample(words_list, length)
    sentence = ' '.join(random_words).lower()
    return sentence

def main():
    print("This program generates a random sentence of a specified length.")
    
    try:
        length = int(input("How many words should the sentence have? (Enter a number between 2 and 20): "))
        
        if 2 <= length <= 20:
            words_list = get_words_from_file('/Users/manuel/Desktop/DI-Bootcamp/Week2_Object/D4/ExerciseXP/word_list.rtf')
            sentence = get_random_sentence(length, words_list)
            print(f"Generated Sentence: {sentence}")
        else:
            print("Error: Please enter a number between 2 and 20.")
    except ValueError:
        print("Error: Invalid input. Please enter a valid integer.")

if __name__ == "__main__":
    main()
