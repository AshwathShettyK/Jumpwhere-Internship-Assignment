# Problem: Clone Graph
# Return a deep copy of an undirected graph.

class Node:
    def __init__(self, val=0, neighbors=None):
        self.val = val
        self.neighbors = neighbors or []


def clone_graph(node):
    if not node:
        return None
    clones = {None: None}

    def dfs(curr):
        if curr in clones:
            return clones[curr]
        clone = Node(curr.val)
        clones[curr] = clone
        for nei in curr.neighbors:
            clone.neighbors.append(dfs(nei))
        return clone

    return dfs(node)


if __name__ == '__main__':
    a = Node(1)
    b = Node(2)
    c = Node(3)
    d = Node(4)
    a.neighbors = [b, d]
    b.neighbors = [a, c]
    c.neighbors = [b, d]
    d.neighbors = [a, c]
    print('Sample Input:')
    print('Graph clone example')
    print('\nSample Output:')
    print(clone_graph(a).val)

# Time: O(V+E)
# Space: O(V)