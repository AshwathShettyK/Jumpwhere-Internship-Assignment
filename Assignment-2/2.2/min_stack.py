# Problem: Min Stack
# Support push, pop, top, and getMin in O(1).

class MinStack:
    def __init__(self):
        self.stack = []
        self.mins = []

    def push(self, x):
        self.stack.append(x)
        self.mins.append(x if not self.mins or x <= self.mins[-1] else self.mins[-1])

    def pop(self):
        self.stack.pop()
        self.mins.pop()

    def top(self):
        return self.stack[-1]

    def get_min(self):
        return self.mins[-1]


if __name__ == '__main__':
    s = MinStack()
    s.push(3)
    s.push(2)
    s.push(1)
    print('Sample Input:')
    print('push 3, push 2, push 1')
    print('\nSample Output:')
    print(s.get_min())
    s.pop()
    print(s.top())

# Time: O(1)
# Space: O(n)