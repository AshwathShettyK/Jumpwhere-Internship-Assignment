# Q10: Unique Sorted Words
# Accept comma-separated words, remove duplicates, sort alphabetically, and print the result.

input_string = input("Enter comma-separated words: ")
word_list = [word.strip() for word in input_string.split(",") if word.strip()]

unique_words = sorted(set(word_list))
result = ",".join(unique_words)

print(f"Unique sorted words: {result}")
