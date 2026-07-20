# Q19: Smallest and Largest Word
# Find and print the smallest and largest word in a sentence.

input_sentence = input("Enter a sentence: ")
words = [word for word in input_sentence.split() if word]

if words:
    smallest_word = min(words, key=len)
    largest_word = max(words, key=len)
    print(f"Smallest word: {smallest_word}")
    print(f"Largest word: {largest_word}")
else:
    print("No words found in the sentence.")
