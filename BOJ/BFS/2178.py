import sys
from collections import deque

input = sys.stdin.readline
dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]

# N = 세로, 행 // M = 가로, 열
N, M = map(int, input().split())
visited = [[False] * M for _ in range(N)]
maze = []

# 미로 입력받기
for _ in range(N):
    maze.append(list(map(int, input().strip())))

queue = deque([(0, 0)])
visited[0][0] = True

while queue:
    x, y = queue.popleft()
    visited[y][x] = True

    for i in range(4):
        mx, ny = x + dx[i], y + dy[i]

        if 0 <= mx < M and 0 <= ny < N and not visited[ny][mx] and maze[ny][mx] == 1:
            maze[ny][mx] += maze[y][x]
            queue.append((mx, ny))
            visited[ny][mx] = True

print(maze[N-1][M-1])