# Q16: Create a list, search for an element, delete it if found, and print the updated list.

input_values = input("Enter list items separated by spaces: ")
items = input_values.split()

search_item = input("Enter the item to search and delete: ")

found_index = None
for index in range(len(items)):
    if items[index] == search_item:
        found_index = index
        break

if found_index is not None:
    del items[found_index]
    print(f"Item '{search_item}' found and deleted.")
    print("Updated list:", items)
else:
    print(f"Item '{search_item}' not found in the list.")
