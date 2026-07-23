# Q1: Sort a dictionary by value in ascending and descending order.

sample_dict = {"a": 3, "b": 1, "c": 2}

sorted_by_value_ascending = dict(sorted(sample_dict.items(), key=lambda item: item[1]))
sorted_by_value_descending = dict(sorted(sample_dict.items(), key=lambda item: item[1], reverse=True))

print("Dictionary sorted by value (ascending):")
print(sorted_by_value_ascending)
print("Dictionary sorted by value (descending):")
print(sorted_by_value_descending)
