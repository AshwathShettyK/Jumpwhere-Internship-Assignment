def generate_parentheses(n):
    out = []

    def backtrack(opened, closed, path):
        if len(path) == 2 * n:
            out.append(path)
            return
        if opened < n:
            backtrack(opened + 1, closed, path + "(")
        if closed < opened:
            backtrack(opened, closed + 1, path + ")")

    backtrack(0, 0, "")
    return out


if __name__ == "__main__":
    n = 3
    print("Sample Input:")
    print(f"n = {n}")
    print("\nSample Output:")
    print(generate_parentheses(n))
