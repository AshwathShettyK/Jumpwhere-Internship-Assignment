# Problem: Top K Frequent Elements
# Return the k most frequent values.

from collections import Counter


def top_k_frequent(nums, k):
    return [v for v, _ in Counter(nums).most_common(k)]


if __name__ == '__main__':
    nums = [1, 1, 1, 2, 2, 3]
    k = 2
    print('Sample Input:')
    print(f'nums = {nums}')
    print(f'k = {k}')
    print('\nSample Output:')
    print(top_k_frequent(nums, k))

# Time: O(n log k)
# Space: O(n)