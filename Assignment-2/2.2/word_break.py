# Problem: Word Break
# Check if a string can be segmented by dictionary words.

def word_break(s, word_dict):
    dp = [False] * (len(s) + 1)
    dp[0] = True
    for i in range(1, len(s) + 1):
        for w in word_dict:
            if i >= len(w) and dp[i - len(w)] and s[i - len(w):i] == w:
                dp[i] = True
                break
    return dp[-1]


if __name__ == '__main__':
    s = 'leetcode'
    word_dict = ['leet', 'code']
    print('Sample Input:')
    print(f's = {s}')
    print(f'word_dict = {word_dict}')
    print('\nSample Output:')
    print(word_break(s, word_dict))

# Time: O(n * m * k)
# Space: O(n)