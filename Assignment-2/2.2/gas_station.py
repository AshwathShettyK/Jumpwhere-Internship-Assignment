# Problem: Gas Station
# Check if a complete circuit is possible.

def can_complete_circuit(gas, cost):
    total = tank = 0
    for g, c in zip(gas, cost):
        total += g - c
        tank += g - c
        if tank < 0:
            tank = 0
    return total >= 0


if __name__ == '__main__':
    gas = [1, 2, 3, 4, 5]
    cost = [3, 4, 5, 1, 2]
    print('Sample Input:')
    print(f'gas = {gas}')
    print(f'cost = {cost}')
    print('\nSample Output:')
    print(can_complete_circuit(gas, cost))

# Time: O(n)
# Space: O(1)