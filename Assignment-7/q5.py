# Q5: Iterate through a dictionary and print keys, values, and key-value pairs.

sample_dict = {"name": "Alice", "age": 25, "city": "Mumbai"}

print("Keys:")
for key in sample_dict:
    print(key)

print("\nValues:")
for value in sample_dict.values():
    print(value)

print("\nKey-Value pairs:")
for key, value in sample_dict.items():
    print(f"{key}: {value}")
