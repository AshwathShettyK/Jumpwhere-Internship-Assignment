# Q2: Character Frequency
# Count the frequency of every character in a string and print a dictionary.

input_string = input("Enter a string: ")

frequency = {}
for character in input_string:
    if character in frequency:
        frequency[character] += 1
    else:
        frequency[character] = 1

print("Character frequency:", frequency)
