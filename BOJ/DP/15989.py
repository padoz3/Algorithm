import sys

input = sys.stdin.readline

T = int(input())

num_list = []
dp = [0] * 10001

dp[0] = 1

for i in [1, 2, 3]:
    for j in range(i, 10001):
        dp[j] += dp[j - i]

for _ in range(T):
    n = int(input())
    print(dp[n])