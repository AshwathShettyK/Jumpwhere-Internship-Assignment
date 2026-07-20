# Q19: Find all strings containing a given substring using lambda and filter().

words = ['red', 'black', 'white', 'green', 'orange']
substring = input("Enter the substring to search: ")

matching_words = list(filter(lambda word: substring in word, words))
print("Matching strings:")
print(matching_words)
