import sys
from collections import deque
input = sys.stdin.readline
sys.setrecursionlimit(1000000)
maps = []

n = int(input())
for _ in range(n):
    maps.append(list(map(int, input().split())))

dp = [[-1] * n for _ in range(n)]

def dfs(y, x):
    if y == n-1 and x == n-1:
        return 1
    if dp[y][x] != -1:
        return dp[y][x]
    dp[y][x] = 0

    curr = maps[y][x]
    if 0 < x + curr < n:
        dp[y][x] += dfs(y, curr+x)
    if 0 < y + curr < n:
        dp[y][x] += dfs(y+curr, x)
    return dp[y][x]

print(dfs(0, 0))