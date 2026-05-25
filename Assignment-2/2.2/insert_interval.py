# Problem: Insert Interval
# Insert and merge a new interval into a sorted list.

def insert_interval(intervals, new_interval):
    res = []
    i = 0
    while i < len(intervals) and intervals[i][1] < new_interval[0]:
        res.append(intervals[i])
        i += 1
    while i < len(intervals) and intervals[i][0] <= new_interval[1]:
        new_interval = [min(new_interval[0], intervals[i][0]), max(new_interval[1], intervals[i][1])]
        i += 1
    res.append(new_interval)
    res.extend(intervals[i:])
    return res


if __name__ == '__main__':
    intervals = [[1, 3], [6, 9]]
    new_interval = [2, 5]
    print('Sample Input:')
    print(f'intervals = {intervals}')
    print(f'new_interval = {new_interval}')
    print('\nSample Output:')
    print(insert_interval(intervals, new_interval))

# Time: O(n)
# Space: O(n)