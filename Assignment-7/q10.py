# Q10: Remove a specified key from a dictionary if it exists.

sample_dict = {"a": 100, "b": 200, "c": 300}
key_to_remove = input("Enter the key to remove: ")

if key_to_remove in sample_dict:
    del sample_dict[key_to_remove]
    print(f"Key '{key_to_remove}' removed.")
    print("Updated dictionary:", sample_dict)
else:
    print(f"Key '{key_to_remove}' not found in the dictionary.")
