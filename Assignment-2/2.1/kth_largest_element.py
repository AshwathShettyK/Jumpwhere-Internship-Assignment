import heapq


def kth_largest(nums, k):
    if not 1 <= k <= len(nums):
        raise ValueError
    return heapq.nlargest(k, nums)[-1]


if __name__ == "__main__":
    nums = [3, 2, 1, 5, 6, 4]
    k = 2
    print("Sample Input:")
    print(f"Array: {nums}")
    print(f"k: {k}")
    print("\nSample Output:")
    print(f"The {k}nd largest element is: {kth_largest(nums, k)}")
