import sys
from collections import deque

input = sys.stdin.readline

dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]

T = int(input())

def bfs(start_x, start_y, visited, n, m, cabbages):
    queue = deque([(start_x, start_y)])
    visited[start_y][start_x] = True

    while queue:
        x, y = queue.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < m and 0 <= ny < n and cabbages[ny][nx] == 1:
                if not visited[ny][nx]:
                    visited[ny][nx] = True
                    queue.append((nx, ny))

for _ in range(T):
    M, N, K = map(int, input().split())
    visited = [[False] * M for _ in range(N)]
    cabbages = [[0] * M for _ in range(N)]
    count = 0

    for i in range(K):
        a, b = map(int, input().split())
        cabbages[b][a] = 1

    for i in range(N):
        for j in range(M):
            if cabbages[i][j] == 1 and visited[i][j] == False:
                bfs(j, i, visited, N, M, cabbages)
                count += 1

    print(count)