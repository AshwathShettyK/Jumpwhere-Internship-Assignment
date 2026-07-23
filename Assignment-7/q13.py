# Q13: Remove duplicate values from a dictionary, keeping the first occurrence.

sample_dict = {"a": 100, "b": 200, "c": 100, "d": 300, "e": 200}
unique_values = set()
new_dict = {}

for key, value in sample_dict.items():
    if value not in unique_values:
        new_dict[key] = value
        unique_values.add(value)

print("Dictionary after removing duplicate values:")
print(new_dict)
