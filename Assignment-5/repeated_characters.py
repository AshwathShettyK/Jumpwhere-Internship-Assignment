# Q15: Repeated Characters
# Count repeated characters and print only those occurring more than once.

input_string = input("Enter a string: ")

character_counts = {}
for character in input_string:
    character_counts[character] = character_counts.get(character, 0) + 1

repeated = [char for char, count in character_counts.items() if count > 1]
print(f"Repeated characters: {repeated}")
