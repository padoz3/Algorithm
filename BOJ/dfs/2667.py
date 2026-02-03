import sys

input = sys.stdin.readline

N = int(input())
visited = [[False] * (N + 1) for _ in range( N + 1)]
ans = []

layout = []
dy = [+1, -1, 0, 0]
dx = [0, 0, -1, +1]

for _ in range(N):
    layout.append(list(input().strip()))

def dfs(x, y):
    stack = [(x, y)]
    visited[x][y] = True
    cnt = 1

    while stack:
        curr_x, curr_y = stack.pop()

        for i in range(4):
            nx = curr_x + dx[i]
            ny = curr_y + dy[i]

            if 0 <= nx < N and 0 <= ny < N:
                if not visited[nx][ny] and layout[nx][ny] == '1':
                    stack.append((nx, ny))
                    cnt += 1
                    visited[nx][ny] = True
    return cnt

ans = []

for i in range(N):
    for j in range(N):
        if not visited[i][j] and layout[i][j] == '1':
            ans.append(dfs(i, j))

ans.sort()

print(len(ans))
for x in ans:
    print(x)