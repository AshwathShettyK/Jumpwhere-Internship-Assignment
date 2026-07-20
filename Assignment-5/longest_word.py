# Q8: Longest Word Length
# Accept a list of words and return the length of the longest word.

input_words = input("Enter words separated by spaces: ")
word_list = input_words.split()

max_length = 0
for word in word_list:
    if len(word) > max_length:
        max_length = len(word)

print(f"Length of the longest word: {max_length}")
