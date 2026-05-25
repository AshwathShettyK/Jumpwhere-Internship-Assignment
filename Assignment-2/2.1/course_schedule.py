from collections import defaultdict, deque


def can_finish(n, prereq):
    g = defaultdict(list)
    indeg = [0] * n
    for a, b in prereq:
        g[b].append(a)
        indeg[a] += 1
    q = deque(i for i, x in enumerate(indeg) if x == 0)
    done = 0
    while q:
        x = q.popleft()
        done += 1
        for y in g[x]:
            indeg[y] -= 1
            if indeg[y] == 0:
                q.append(y)
    return done == n


if __name__ == "__main__":
    n = 4
    prereq = [[1, 0], [2, 1], [3, 2]]
    print("Sample Input:")
    print(f"Courses: {n}")
    print(f"Prerequisites: {prereq}")
    print("\nSample Output:")
    print(f"Can finish all courses? {can_finish(n, prereq)}")
