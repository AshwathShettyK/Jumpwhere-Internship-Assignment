# Problem: Course Schedule
# Check if all courses can be finished.

from collections import defaultdict, deque


def can_finish(num_courses, prerequisites):
    graph = defaultdict(list)
    indeg = [0] * num_courses
    for a, b in prerequisites:
        graph[b].append(a)
        indeg[a] += 1
    q = deque(i for i, x in enumerate(indeg) if x == 0)
    done = 0
    while q:
        x = q.popleft()
        done += 1
        for y in graph[x]:
            indeg[y] -= 1
            if indeg[y] == 0:
                q.append(y)
    return done == num_courses


if __name__ == '__main__':
    num_courses = 2
    prerequisites = [[1, 0]]
    print('Sample Input:')
    print(f'courses = {num_courses}')
    print(f'prerequisites = {prerequisites}')
    print('\nSample Output:')
    print(can_finish(num_courses, prerequisites))

# Time: O(V+E)
# Space: O(V+E)