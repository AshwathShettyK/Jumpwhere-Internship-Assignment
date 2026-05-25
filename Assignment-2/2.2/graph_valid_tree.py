# Problem: Graph Valid Tree
# Check whether a graph is a valid tree.

class DSU:
    def __init__(self, n):
        self.parent = list(range(n))
        self.rank = [0] * n

    def find(self, x):
        while self.parent[x] != x:
            self.parent[x] = self.parent[self.parent[x]]
            x = self.parent[x]
        return x

    def union(self, a, b):
        ra, rb = self.find(a), self.find(b)
        if ra == rb:
            return False
        if self.rank[ra] < self.rank[rb]:
            ra, rb = rb, ra
        self.parent[rb] = ra
        if self.rank[ra] == self.rank[rb]:
            self.rank[ra] += 1
        return True


def valid_tree(n, edges):
    if len(edges) != n - 1:
        return False
    dsu = DSU(n)
    for a, b in edges:
        if not dsu.union(a, b):
            return False
    return True


if __name__ == '__main__':
    n = 5
    edges = [[0, 1], [0, 2], [0, 3], [1, 4]]
    print('Sample Input:')
    print(f'n = {n}')
    print(f'edges = {edges}')
    print('\nSample Output:')
    print(valid_tree(n, edges))

# Time: O(E alpha(V))
# Space: O(V)