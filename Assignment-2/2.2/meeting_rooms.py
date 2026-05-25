# Problem: Meeting Rooms
# Check if one person can attend all meetings.

def can_attend_meetings(intervals):
    intervals.sort()
    for i in range(1, len(intervals)):
        if intervals[i][0] < intervals[i - 1][1]:
            return False
    return True


if __name__ == '__main__':
    intervals = [[0, 30], [5, 10], [15, 20]]
    print('Sample Input:')
    print(intervals)
    print('\nSample Output:')
    print(can_attend_meetings(intervals))

# Time: O(n log n)
# Space: O(1)