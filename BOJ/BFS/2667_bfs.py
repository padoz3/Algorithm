import sys
from collections import deque
input = sys.stdin.readline

N = int(input())
apart = []
dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]
visited = [[False] * N for _ in range(N)]

# bfs 함수 정리하기
def bfs(start_x, start_y, visited, apart, n):
    queue = deque([(start_x, start_y)])
    visited[start_y][start_x] = True
    count = 0

    while queue:
        count += 1
        x, y = queue.popleft()
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if 0 <= nx < n and 0 <= ny < n and not visited[ny][nx]:
                if apart[ny][nx] == 1:
                    visited[ny][nx] = True
                    queue.append((nx, ny))

    return count

complex = []
# 입력받기
for _ in range(N):
    apart.append(list(map(int, input().strip())))

# i = 세로, 행 // j = 가로, 열
for i in range(N):
    for j in range(N):
        if apart[i][j] == 1 and not visited[i][j]:
            complex.append(bfs(j, i, visited, apart, N))
complex.sort()
print(len(complex))
for a in complex:
    print(a)