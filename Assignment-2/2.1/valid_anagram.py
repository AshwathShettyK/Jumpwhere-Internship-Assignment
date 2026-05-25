from collections import Counter


def is_valid_anagram(a, b):
    return len(a) == len(b) and Counter(a) == Counter(b)


if __name__ == "__main__":
    samples = [("listen", "silent"), ("hello", "world")]
    print("Sample Input:")
    for i, (a, b) in enumerate(samples, 1):
        print(f"{i}) {a}, {b}")
    print("\nSample Output:")
    for i, (a, b) in enumerate(samples, 1):
        print(f"{i}) {a} and {b} -> {is_valid_anagram(a, b)}")
