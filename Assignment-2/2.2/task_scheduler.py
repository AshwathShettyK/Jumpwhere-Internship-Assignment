# Problem: Task Scheduler
# Minimize the intervals between identical tasks.

from collections import Counter
import heapq


def least_interval(tasks, n):
    counts = Counter(tasks)
    heap = [-c for c in counts.values()]
    heapq.heapify(heap)
    time = 0
    while heap:
        block = []
        for _ in range(n + 1):
            if not heap:
                break
            cnt = -heapq.heappop(heap)
            cnt -= 1
            if cnt:
                block.append(cnt)
            time += 1
        for cnt in block:
            heapq.heappush(heap, -cnt)
        if not heap and not block:
            break
    return time


if __name__ == '__main__':
    tasks = ['A', 'A', 'A', 'B', 'B', 'B']
    n = 2
    print('Sample Input:')
    print(f'tasks = {tasks}')
    print(f'n = {n}')
    print('\nSample Output:')
    print(least_interval(tasks, n))

# Time: O(n log k)
# Space: O(k)