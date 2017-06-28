def number_of_coins(coins, n):
    coins.sort()
    r, c = len(coins), n+1
    ways = [1] * c
    for k in range(1, c):
        if k % coins[0] != 0:
            ways[k] = 0
    for i in range(1, r):
        for j in range(coins[i], c):
            ways[j] += ways[j - coins[i]]
    return ways[c-1]

t, m = map(int, input().split())
coin = []
coin = list(map(int, input().split()))
print(number_of_coins(coin, t))