# Q13: Sort a list of dictionaries using lambda based on model.

phones = [
    {'make': 'Nokia', 'model': 216, 'color': 'Black'},
    {'make': 'Mi Max', 'model': 2, 'color': 'Gold'},
    {'make': 'Samsung', 'model': 7, 'color': 'Blue'}
]

sorted_phones = sorted(phones, key=lambda item: item['model'])
print("Sorted list based on model:")
print(sorted_phones)
