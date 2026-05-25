# Problem: Container With Most Water
# Find the maximum area between two heights.

def max_area(height):
    left, right = 0, len(height) - 1
    best = 0
    while left < right:
        best = max(best, min(height[left], height[right]) * (right - left))
        if height[left] <= height[right]:
            left += 1
        else:
            right -= 1
    return best


if __name__ == '__main__':
    height = [1, 8, 6, 2, 5, 4, 8, 3, 7]
    print('Sample Input:')
    print(height)
    print('\nSample Output:')
    print(max_area(height))

# Time: O(n)
# Space: O(1)