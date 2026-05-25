from math import factorial


def get_kth_permutation(n, k):
    if not 1 <= k <= factorial(n):
        raise ValueError
    nums = list(range(1, n + 1))
    k -= 1
    out = []
    for i in range(n, 0, -1):
        block = factorial(i - 1)
        out.append(str(nums.pop(k // block)))
        k %= block
    return "".join(out)


if __name__ == "__main__":
    n = 4
    k = 9
    print("Sample Input:")
    print(f"n = {n}")
    print(f"k = {k}")
    print("\nSample Output:")
    print(f"The {k}th permutation is: {get_kth_permutation(n, k)}")
