# Q16: Filter numbers divisible by 19 or 13 using lambda and filter().

numbers = [19, 65, 57, 39, 152, 639, 121, 44, 90, 190]
filtered_numbers = list(filter(lambda x: x % 19 == 0 or x % 13 == 0, numbers))
print("Numbers divisible by 19 or 13:")
print(filtered_numbers)
