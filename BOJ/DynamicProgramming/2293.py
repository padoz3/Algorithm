import sys

input = sys.stdin.readline

n, k = map(int, input().split())
coin_list = []
dp = [0] * 100001

for _ in range(n):
    coin = int(input())
    if coin > 0:
        coin_list.append(coin)

coin_list.sort()

dp[0] = 1

for coin in coin_list:
    for i in range( k + 1):
        dp[i] = dp[i] + dp[i - coin]
    
print(dp[i])