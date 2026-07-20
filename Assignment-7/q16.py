# Q16: Find the highest three values in a dictionary and display them in descending order.

sample_dict = {"a": 100, "b": 300, "c": 200, "d": 400, "e": 150}

sorted_values = sorted(sample_dict.values(), reverse=True)
highest_three = sorted_values[:3]

print("Highest three values in descending order:")
print(highest_three)
