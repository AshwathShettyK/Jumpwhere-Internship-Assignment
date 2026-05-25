# Problem: Merge Intervals
# Merge overlapping intervals.

def merge_intervals(intervals):
    intervals.sort()
    merged = []
    for start, end in intervals:
        if not merged or start > merged[-1][1]:
            merged.append([start, end])
        else:
            merged[-1][1] = max(merged[-1][1], end)
    return merged


if __name__ == '__main__':
    intervals = [[1, 3], [2, 6], [8, 10], [15, 18]]
    print('Sample Input:')
    print(intervals)
    print('\nSample Output:')
    print(merge_intervals(intervals))

# Time: O(n log n)
# Space: O(n)