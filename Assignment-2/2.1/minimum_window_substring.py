from collections import Counter


def min_window(s, t):
    if not s or not t:
        return ""
    need = Counter(t)
    have = Counter()
    left = 0
    matched = 0
    best = ""
    for right, ch in enumerate(s):
        have[ch] += 1
        if have[ch] == need[ch]:
            matched += 1
        while matched == len(need):
            if not best or right - left + 1 < len(best):
                best = s[left:right + 1]
            left_ch = s[left]
            have[left_ch] -= 1
            if have[left_ch] < need[left_ch]:
                matched -= 1
            left += 1
    return best


if __name__ == "__main__":
    s = "ADOBECODEBANC"
    t = "ABC"
    print("Sample Input:")
    print(f"s = {s}")
    print(f"t = {t}")
    print("\nSample Output:")
    print(f"Minimum window: {min_window(s, t)}")
