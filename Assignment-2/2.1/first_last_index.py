from bisect import bisect_left, bisect_right


def first_last_index(nums, target):
    left = bisect_left(nums, target)
    if left == len(nums) or nums[left] != target:
        return [-1, -1]
    return [left, bisect_right(nums, target) - 1]


if __name__ == "__main__":
    nums = [1, 2, 4, 4, 4, 5, 6]
    target = 4
    print("Sample Input:")
    print(f"Array: {nums}")
    print(f"Target: {target}")
    print("\nSample Output:")
    print(f"First and last index -> {first_last_index(nums, target)}")
