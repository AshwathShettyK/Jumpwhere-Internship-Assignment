# Q20: Sort a mixed list containing integers and strings using lambda.

mixed_list = [19, 'red', 12, 'green', 'blue', 10, 'white', 'green', 1]

sorted_numbers = sorted([item for item in mixed_list if isinstance(item, int)])
sorted_strings = sorted([item for item in mixed_list if isinstance(item, str)])
result_list = sorted_numbers + sorted_strings

print("Sorted mixed list:")
print(result_list)
