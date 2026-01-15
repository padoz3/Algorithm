import sys

input = sys.stdin.readline

N = int(input())
dp = [0] * (N + 1)

for i in range(2, N + 1):
    if i % 3 == 0:
       i_3 = i // 3
    else: i_3 = 0

    if i % 2 == 0:
        i_2 = i // 2
    else:
        i_2 = 0

    if i_2 and i_3:
        dp[i] = min(dp[i_3], dp[i_2], dp[i - 1]) + 1
    elif i_3:
        dp[i] = min(dp[i_3], dp[i - 1]) + 1
    elif i_2:
        dp[i] = min(dp[i_2], dp[i - 1]) + 1
    else:
        dp[i] = dp[i-1] + 1
print(dp[N])