import tkinter as tk
from tkinter import messagebox
from anagram_checker import AnagramChecker

class AnagramApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Anagram Checker")
        
        # Create and place widgets
        self.label = tk.Label(root, text="Enter a word:")
        self.label.pack(pady=10)
        
        self.entry = tk.Entry(root, width=50)
        self.entry.pack(pady=10)
        
        self.check_button = tk.Button(root, text="Check Anagrams", command=self.check_anagrams)
        self.check_button.pack(pady=10)
        
        self.result_label = tk.Label(root, text="", wraplength=400)
        self.result_label.pack(pady=10)
        
    def check_anagrams(self):
        word = self.entry.get().strip().upper()
        if self.validate_input(word):
            checker = AnagramChecker()
            if checker.is_valid_word(word):
                anagrams = checker.get_anagrams(word)
                if anagrams:
                    result = f"YOUR WORD: \"{word}\"\nThis is a valid English word.\nAnagrams for your word: {', '.join(anagrams)}"
                else:
                    result = f"YOUR WORD: \"{word}\"\nThis is a valid English word.\nNo anagrams found."
            else:
                result = f"\"{word}\" is not a valid English word."
            self.result_label.config(text=result)
        else:
            messagebox.showerror("Invalid Input", "Please enter a single word with alphabetic characters only.")
    
    def validate_input(self, word):
        if len(word.split()) > 1:
            return False
        if not word.isalpha():
            return False
        return True

if __name__ == "__main__":
    root = tk.Tk()
    app = AnagramApp(root)
    root.mainloop()

python /Users/manuel/Desktop/DI-Bootcamp/Week2_Object/D5/ExerciseXP/anagrams_tkinter.py
