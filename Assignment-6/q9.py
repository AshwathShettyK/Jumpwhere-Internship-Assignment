# Q9: Calculate total, discount, and final amount for shop purchases.

try:
    quantity = int(input("Enter the quantity of items purchased: "))
except ValueError:
    print("Invalid input. Please enter an integer quantity.")
    raise SystemExit

if quantity < 0:
    print("Quantity cannot be negative.")
    raise SystemExit

unit_price = 100
total_amount = quantity * unit_price

discount = 0
if total_amount > 1000:
    discount = total_amount * 0.10

final_amount = total_amount - discount

print(f"Total amount: {total_amount}")
print(f"Discount: {discount}")
print(f"Final amount to pay: {final_amount}")
