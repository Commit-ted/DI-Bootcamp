class AnagramChecker:
    def __init__(self, word_list_file='/Users/manuel/Desktop/DI-Bootcamp/Week2_Object/D5/ExerciseXP/cleaned_wordlist.txt'):
        """Load the word list file into a variable."""
        with open(word_list_file, 'r') as file:
            self.word_list = set(file.read().splitlines())
            #print(self.word_list) #To check the acces to the list

    def is_valid_word(self, word):
        """Check if the given word is a valid word in the word list."""
        return word.upper() in self.word_list
    
    def is_anagram(self, word1, word2):
        """Check if two words are anagrams."""
        return sorted(word1.upper()) == sorted(word2.upper())
    
    def get_anagrams(self, word):
        """Find all anagrams of the given word in the word list."""
        word = word.upper()
        anagrams = [w for w in self.word_list if self.is_anagram(word, w) and w != word]
        return anagrams
    
    # Create an instance of AnagramChecker
checker = AnagramChecker()

# Check if a word is valid
print(checker.is_valid_word('meat'))  # True or False

# Get all anagrams of a word
print(checker.get_anagrams('meat'))  # ['MATE', 'TAME', 'TEAM'] if those are in the word list

