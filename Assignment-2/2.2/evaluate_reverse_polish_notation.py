# Problem: Evaluate Reverse Polish Notation
# Evaluate an expression written in postfix form.


def eval_rpn(tokens):
    stack = []
    ops = {'+': lambda a, b: a + b, '-': lambda a, b: b - a, '*': lambda a, b: a * b, '/': lambda a, b: int(b / a)}
    for t in tokens:
        if t in ops:
            b = stack.pop()
            a = stack.pop()
            stack.append(ops[t](a, b))
        else:
            stack.append(int(t))
    return stack[0]


if __name__ == '__main__':
    tokens = ['2', '1', '+', '3', '*']
    print('Sample Input:')
    print(tokens)
    print('\nSample Output:')
    print(eval_rpn(tokens))

# Time: O(n)
# Space: O(n)