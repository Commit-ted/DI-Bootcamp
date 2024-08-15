# anagrams.py
from anagram_checker import AnagramChecker

def main_menu():
    while True:
        print("\n--- Anagram Checker ---")
        print("1. Input a word")
        print("2. Exit")
        choice = input("Please choose an option: ").strip()
        
        if choice == '1':
            word_input()
        elif choice == '2':
            print("Goodbye!")
            break
        else:
            print(f"Invalid option '{choice}', please try again.")

def word_input():
    word = input("Please enter a single word: ").strip()
    
    if validate_input(word):
        word = word.upper()  # Convert word to uppercase to ensure consistency
        checker = AnagramChecker()
        if checker.is_valid_word(word):
            anagrams = checker.get_anagrams(word)
            print(f"\nYOUR WORD: \"{word}\"")
            print("This is a valid English word.")
            if anagrams:
                print(f"Anagrams for your word: {', '.join(anagrams)}")
            else:
                print("No anagrams found for your word.")
        else:
            print(f"\"{word}\" is not a valid English word.")
    else:
        print("Invalid input. Please enter a single word with alphabetic characters only.")

def validate_input(word):
    if len(word.split()) > 1:
        print("Error: Please enter only one word.")
        return False
    if not word.isalpha():
        print("Error: Please enter only alphabetic characters.")
        return False
    return True

if __name__ == "__main__":
    main_menu()
