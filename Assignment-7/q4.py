# Q4: Check whether a given key exists in a dictionary.

sample_dict = {"name": "Alice", "age": 25, "city": "Mumbai"}

search_key = input("Enter the key to search: ")

if search_key in sample_dict:
    print(f"The key '{search_key}' exists in the dictionary.")
else:
    print(f"The key '{search_key}' does not exist in the dictionary.")
