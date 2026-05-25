# Problem: Coin Change
# Find the minimum number of coins to make the amount.

def coin_change(coins, amount):
    dp = [amount + 1] * (amount + 1)
    dp[0] = 0
    for x in range(1, amount + 1):
        for c in coins:
            if x >= c:
                dp[x] = min(dp[x], dp[x - c] + 1)
    return dp[amount] if dp[amount] <= amount else -1


if __name__ == '__main__':
    coins = [1, 2, 5]
    amount = 11
    print('Sample Input:')
    print(f'coins = {coins}')
    print(f'amount = {amount}')
    print('\nSample Output:')
    print(coin_change(coins, amount))

# Time: O(amount * len(coins))
# Space: O(amount)