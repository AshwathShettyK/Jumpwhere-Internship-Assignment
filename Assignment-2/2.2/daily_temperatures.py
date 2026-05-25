# Problem: Daily Temperatures
# Return days until a warmer temperature appears.

def daily_temperatures(temp):
    stack = []
    ans = [0] * len(temp)
    for i, t in enumerate(temp):
        while stack and temp[stack[-1]] < t:
            idx = stack.pop()
            ans[idx] = i - idx
        stack.append(i)
    return ans


if __name__ == '__main__':
    temp = [73, 74, 75, 71, 69, 72, 76, 73]
    print('Sample Input:')
    print(temp)
    print('\nSample Output:')
    print(daily_temperatures(temp))

# Time: O(n)
# Space: O(n)