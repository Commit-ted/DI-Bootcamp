def sort_words(input_str):
    # Splitting the input string by commas and using list comprehension to strip and sort
    sorted_words = sorted([word.strip() for word in input_str.split(",")])
    # Joining the sorted list back into a comma-separated string
    return ",".join(sorted_words)

# Example usage
input_str = "without,hello,bag,world"
print(sort_words(input_str))


def longest_word(sentence):
    # Splitting the sentence into words based on spaces
    words = sentence.split()
    # Finding the longest word using max with key as length of words
    longest = max(words, key=len)
    return longest

# Example usage
print(longest_word("Margaret's toy is a pretty doll."))
print(longest_word("A thing of beauty is a joy forever."))
print(longest_word("Forgetfulness is by all means powerless!"))
