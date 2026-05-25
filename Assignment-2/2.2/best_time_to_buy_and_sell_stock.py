# Problem: Best Time to Buy and Sell Stock
# Maximize profit with one buy and one sell.

def max_profit(prices):
    min_price = prices[0]
    best = 0
    for p in prices[1:]:
        min_price = min(min_price, p)
        best = max(best, p - min_price)
    return best


if __name__ == '__main__':
    prices = [7, 1, 5, 3, 6, 4]
    print('Sample Input:')
    print(prices)
    print('\nSample Output:')
    print(max_profit(prices))

# Time: O(n)
# Space: O(1)