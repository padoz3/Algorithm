import sys
from collections import deque
input = sys.stdin.readline

N = int(input())
realm = []
rain = 0
not_flooded_realm = []
visited = [[False] * N for _ in range(N)]
dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]

def bfs(start_x, start_y, realm, visited, n, rain):
    queue = deque([(start_x, start_y)])
    visited[start_y][start_x] = True

    while queue:
        x, y = queue.popleft()
        # print((x, y), end=' ')
        for k in range(4):
            nx, ny = x + dx[k], y + dy[k]
            if 0 <= nx < n and 0 <= ny < n and not visited[ny][nx] and realm[ny][nx] > rain:
                visited[ny][nx] = True
                queue.append((nx, ny))

for _ in range(N):
    a = [*map(int, input().split())]
    realm.append(a)
max_rain = max(max(row) for row in realm)

# for i in range(N):
#     for j in range(N):
#         print(realm[i][j] - 3, end=' ')
#     print()

while rain < max_rain:
    # print(rain)
    count = 0
    for i in range(N):
        for j in range(N):
            if realm[i][j] > rain and not visited[i][j]:
                visited[i][j] = True
                bfs(j, i, realm, visited, N, rain)
                count += 1
    not_flooded_realm.append(count)
    rain += 1
    visited = [[False] * N for _ in range(N)]
    # print()

print(max(not_flooded_realm))