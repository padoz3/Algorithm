import sys
sys.setrecursionlimit(10000)
input = sys.stdin.readline

dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]

def dfs(x, y, visited, n, m):
    visited[y][x] = True
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        if 0 <= nx < m and 0 <= ny < n and visited[ny][nx] == False:
            if cabbages[ny][nx] == 1:
                dfs(nx, ny, visited, n, m)

T = int(input())

for _ in range(T):
    M, N, K = map(int, input().split())
    cabbages = [[0] * M for _ in range(N)]
    visited = [[False] * M for _ in range(N)]
    count = 0

    # 양배추 추가
    for i in range(K):
        x, y = map(int, input().split())
        cabbages[y][x] = 1

    for i in range(N):
        for j in range(M):
            if visited[i][j] == False and cabbages[i][j] == 1:
                dfs(j, i, visited, N, M)
                count += 1
        
    print(count)
