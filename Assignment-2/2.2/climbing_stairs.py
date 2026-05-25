# Problem: Climbing Stairs
# Count the number of ways to reach the top.

def climb_stairs(n):
    a, b = 1, 1
    for _ in range(n):
        a, b = b, a + b
    return a


if __name__ == '__main__':
    n = 5
    print('Sample Input:')
    print(f'n = {n}')
    print('\nSample Output:')
    print(climb_stairs(n))

# Time: O(n)
# Space: O(1)