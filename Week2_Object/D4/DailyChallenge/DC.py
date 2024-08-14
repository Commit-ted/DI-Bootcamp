import os

#1
# class Text:
#     def __init__(self, text):
#         self.text = text.lower()
#         self.words = self.text.split()

#     def word_frequency(self, word):
#         word = word.lower()
#         frequency = self.words.count(word)
#         if frequency > 0:
#             return frequency
#         else:
#             return f"The word '{word}' does not exist in the text."

#     def most_common_word(self):
#         from collections import Counter
#         word_counts = Counter(self.words)
#         most_common = word_counts.most_common(1)
#         if most_common:
#             return most_common[0][0]
#         else:
#             return "No words found in the text."

#     def unique_words(self):
#         return list(set(self.words))

# # Example usage:
# text_example = "A good book would sometimes cost as much as a good house."
# text_obj = Text(text_example)

# print(text_obj.word_frequency("good"))  # Output: 2
# print(text_obj.most_common_word())      # Output: "a"
# print(text_obj.unique_words())          # Output: ['as', 'a', 'book', 'house', 'sometimes', 'would', 'good', 'much', 'cost']


#2
class Text:
    def __init__(self, text):
        self.text = text.lower()
        self.words = self.text.split()

    def word_frequency(self, word):
        word = word.lower()
        frequency = self.words.count(word)
        if frequency > 0:
            return frequency
        else:
            return f"The word '{word}' does not exist in the text."

    def most_common_word(self):
        from collections import Counter
        word_counts = Counter(self.words)
        most_common = word_counts.most_common(1)
        if most_common:
            return most_common[0][0]
        else:
            return "No words found in the text."

    def unique_words(self):
        return list(set(self.words))

    @classmethod
    def from_file(cls, file_path):
        with open(file_path, 'r', encoding='utf-8') as file:
            text = file.read()
        return cls(text)

# Example usage:
file_path = '/Users/manuel/Desktop/DI-Bootcamp/Week2_Object/D4/DailyChallenge/the_stranger.txt'
text_obj_from_file = Text.from_file(file_path)

# print(text_obj_from_file.word_frequency("stranger"))
# print(text_obj_from_file.most_common_word())
# print(text_obj_from_file.unique_words())

#3
import string

class Text:
    def __init__(self, text):
        self.text = text.lower()
        self.words = self.text.split()

    def word_frequency(self, word):
        word = word.lower()
        frequency = self.words.count(word)
        if frequency > 0:
            return frequency
        else:
            return f"The word '{word}' does not exist in the text."

    def most_common_word(self):
        from collections import Counter
        word_counts = Counter(self.words)
        most_common = word_counts.most_common(1)
        if most_common:
            return most_common[0][0]
        else:
            return "No words found in the text."

    def unique_words(self):
        return list(set(self.words))

    @classmethod
    def from_file(cls, file_path):
        with open(file_path, 'r', encoding='utf-8') as file:
            text = file.read()
        return cls(text)


class TextModification(Text):

    def remove_punctuation(self):
        translator = str.maketrans('', '', string.punctuation)
        self.text = self.text.translate(translator)
        self.words = self.text.split()
        return self.text

    def remove_stop_words(self):
        stop_words = {
            'a', 'about', 'above', 'after', 'again', 'against', 'all', 'am', 'an', 'and', 'any', 'are', 'aren\'t', 'as',
            'at', 'be', 'because', 'been', 'before', 'being', 'below', 'between', 'both', 'but', 'by', 'can\'t', 'cannot',
            'could', 'couldn\'t', 'did', 'didn\'t', 'do', 'does', 'doesn\'t', 'doing', 'don\'t', 'down', 'during', 'each',
            'few', 'for', 'from', 'further', 'had', 'hadn\'t', 'has', 'hasn\'t', 'have', 'haven\'t', 'having', 'he', 'he\'d',
            'he\'ll', 'he\'s', 'her', 'here', 'here\'s', 'hers', 'herself', 'him', 'himself', 'his', 'how', 'how\'s', 'i', 'i\'d',
            'i\'ll', 'i\'m', 'i\'ve', 'if', 'in', 'into', 'is', 'isn\'t', 'it', 'it\'s', 'its', 'itself', 'let\'s', 'me', 'more', 'most',
            'mustn\'t', 'my', 'myself', 'no', 'nor', 'not', 'of', 'off', 'on', 'once', 'only', 'or', 'other', 'ought', 'our',
            'ours', 'ourselves', 'out', 'over', 'own', 'same', 'shan\'t', 'she', 'she\'d', 'she\'ll', 'she\'s', 'should', 'shouldn\'t',
            'so', 'some', 'such', 'than', 'that', 'that\'s', 'the', 'their', 'theirs', 'them', 'themselves', 'then', 'there', 'there\'s',
            'these', 'they', 'they\'d', 'they\'ll', 'they\'re', 'they\'ve', 'this', 'those', 'through', 'to', 'too', 'under', 'until',
            'up', 'very', 'was', 'wasn\'t', 'we', 'we\'d', 'we\'ll', 'we\'re', 'we\'ve', 'were', 'weren\'t', 'what', 'what\'s',
            'when', 'when\'s', 'where', 'where\'s', 'which', 'while', 'who', 'who\'s', 'whom', 'why', 'why\'s', 'with',
            'won\'t', 'would', 'wouldn\'t', 'you', 'you\'d', 'you\'ll', 'you\'re', 'you\'ve', 'your', 'yours', 'yourself', 'yourselves'
        }
        filtered_words = [word for word in self.words if word not in stop_words]
        return ' '.join(filtered_words)

    def remove_special_characters(self):
        cleaned_text = ''.join(e for e in self.text if e.isalnum() or e.isspace())
        self.words = cleaned_text.split()
        return cleaned_text

# Example usage:
file_path = '/Users/manuel/Desktop/DI-Bootcamp/Week2_Object/D4/DailyChallenge/the_stranger.txt'
text_mod_obj = TextModification.from_file(file_path)

#print("Text without punctuation:\n", text_mod_obj.remove_punctuation())
#print("\nText without stop words:\n", text_mod_obj.remove_stop_words())
print("\nText without special characters:\n", text_mod_obj.remove_special_characters())
