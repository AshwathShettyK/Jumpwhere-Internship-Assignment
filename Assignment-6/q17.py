# Q17: Create even, odd, and prime lists from range 1 to 100.

numbers = list(range(1, 101))
even_numbers = []
odd_numbers = []
prime_numbers = []

for number in numbers:
    if number % 2 == 0:
        even_numbers.append(number)
    else:
        odd_numbers.append(number)

    if number > 1:
        is_prime = True
        for divisor in range(2, int(number**0.5) + 1):
            if number % divisor == 0:
                is_prime = False
                break
        if is_prime:
            prime_numbers.append(number)

print("Even numbers:", even_numbers)
print("Odd numbers:", odd_numbers)
print("Prime numbers:", prime_numbers)
