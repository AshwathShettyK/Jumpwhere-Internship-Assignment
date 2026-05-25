# Problem: Non-overlapping Intervals
# Remove minimum intervals so no overlaps remain.

def erase_overlap_intervals(intervals):
    intervals.sort(key=lambda x: x[1])
    count = 0
    prev_end = float('-inf')
    for start, end in intervals:
        if start >= prev_end:
            prev_end = end
        else:
            count += 1
    return count


if __name__ == '__main__':
    intervals = [[1, 2], [2, 3], [3, 4], [1, 3]]
    print('Sample Input:')
    print(intervals)
    print('\nSample Output:')
    print(erase_overlap_intervals(intervals))

# Time: O(n log n)
# Space: O(1)