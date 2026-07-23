# Q2: Print numbers from 0 to 6 except 3 and 6 using continue.

for number in range(7):
    if number == 3 or number == 6:
        continue
    print(number)
