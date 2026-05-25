# Problem: Find Median from Data Stream
# Maintain the running median of numbers as they are added.

import heapq

class MedianFinder:
    def __init__(self):
        self.low = []
        self.high = []

    def add_num(self, num):
        heapq.heappush(self.low, -num)
        heapq.heappush(self.high, -heapq.heappop(self.low))
        if len(self.high) > len(self.low):
            heapq.heappush(self.low, -heapq.heappop(self.high))

    def find_median(self):
        if len(self.low) > len(self.high):
            return float(-self.low[0])
        return (-self.low[0] + self.high[0]) / 2


if __name__ == '__main__':
    mf = MedianFinder()
    for num in [1, 2, 3]:
        mf.add_num(num)
    print('Sample Input:')
    print('[1, 2, 3]')
    print('\nSample Output:')
    print(mf.find_median())

# Time: O(log n)
# Space: O(n)