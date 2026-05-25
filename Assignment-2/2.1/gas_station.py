def can_complete_circuit(gas, cost):
    total = 0
    tank = 0
    for g, c in zip(gas, cost):
        total += g - c
        tank += g - c
        if tank < 0:
            tank = 0
    return total >= 0


if __name__ == "__main__":
    gas = [1, 2, 3, 4, 5]
    cost = [3, 4, 5, 1, 2]
    print("Sample Input:")
    print(f"Gas: {gas}")
    print(f"Cost: {cost}")
    print("\nSample Output:")
    print(f"Can complete circuit? {can_complete_circuit(gas, cost)}")
