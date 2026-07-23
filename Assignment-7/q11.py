# Q11: Sort a dictionary by keys in ascending and descending order.

sample_dict = {"c": 3, "a": 1, "b": 2}

sorted_by_key_ascending = dict(sorted(sample_dict.items()))
sorted_by_key_descending = dict(sorted(sample_dict.items(), reverse=True))

print("Dictionary sorted by keys (ascending):")
print(sorted_by_key_ascending)
print("Dictionary sorted by keys (descending):")
print(sorted_by_key_descending)
