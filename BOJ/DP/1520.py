import sys
from collections import deque
sys.setrecursionlimit(1000000)
input = sys.stdin.readline
# n = 행, m = 열
n, m = map(int, input().split())
maps = []
dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]
dp = [[-1] * m for _ in range(n)]
queue = deque([(0, 0)])

for i in range(n):
    maps.append(list(map(int, input().split())))

def dfs(y, x):
    if y == n-1 and x == m-1:
        return 1
    if dp[y][x] != -1:
        return dp[y][x]
    dp[y][x] = 0
    for d in range(4):
        nx, ny = x + dx[d], y + dy[d]
        if 0 <= nx < m and 0 <= ny < n:
            if maps[ny][nx] < maps[y][x]:
                dp[y][x] += dfs(ny, nx)
    return dp[y][x]

print(dfs(0, 0))