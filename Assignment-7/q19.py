# Q19: Remove duplicate lists from a list of lists, preserving the first occurrence.

list_of_lists = [[10, 20], [40], [30, 56, 25], [10, 20], [33], [40]]
unique_lists = []
seen = set()

for inner_list in list_of_lists:
    tuple_form = tuple(inner_list)
    if tuple_form not in seen:
        seen.add(tuple_form)
        unique_lists.append(inner_list)

print("List after removing duplicates:")
print(unique_lists)
