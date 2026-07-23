# Q17: Compare two dictionaries and print keys present in both with the same value.

dict_one = {'key1': 1, 'key2': 2, 'key3': 3}
dict_two = {'key1': 1, 'key2': 20, 'key4': 4}

for key in dict_one:
    if key in dict_two and dict_one[key] == dict_two[key]:
        print(f"{key} : {dict_one[key]} is present in both dictionaries.")
