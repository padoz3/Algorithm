import sys

input = sys.stdin.readline

n, k = map(int, input().split())
coin_list = []
dp = [1e9] * (100001)

for _ in range(n):
    coin = int(input())
    if coin > 0:
        coin_list.append(coin)
        dp[coin] = 1


coin_list.sort(reverse=True)
min_coin = coin_list[-1]

# 목표 금액이 가장 싼 동전보다 낮은 경우, 만들 수 없음.
if k < min_coin:
    print(-1)
else:
    for i in range(min_coin + 1, k + 1):
        count = 0
        for coin in coin_list:
            if i >= coin:
                dp[i] = min(dp[i], dp[i - coin] + 1)
if dp[k] == 1e9:
    print(-1)
else:
    print(dp[k])