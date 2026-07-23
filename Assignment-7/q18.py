# Q18: Check whether all dictionaries inside a list are empty.

sample_list = [{}, {}, {}]

all_empty = all(len(d) == 0 for d in sample_list)
print(all_empty)
