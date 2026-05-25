def largest_rectangle_area(h):
    h = h + [0]
    stack = []
    best = 0
    for i, x in enumerate(h):
        while stack and h[stack[-1]] > x:
            top = stack.pop()
            width = i if not stack else i - stack[-1] - 1
            best = max(best, h[top] * width)
        stack.append(i)
    return best


if __name__ == "__main__":
    heights = [2, 1, 5, 6, 2, 3]
    print("Sample Input:")
    print(f"Heights: {heights}")
    print("\nSample Output:")
    print(f"Largest rectangle area: {largest_rectangle_area(heights)}")
