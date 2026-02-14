import sys

sys.setrecursionlimit(10**6)

input = sys.stdin.readline

dx = [0, 0, -1, +1]
dy = [+1, -1, 0, 0]

def dfs(y, x, n, m, cabbages, visited):
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < m and 0 <= ny < n:
            if cabbages[ny][nx] == 1 and not visited[ny][nx]:
                visited[ny][nx] = True
                dfs(ny, nx, n, m, cabbages, visited)

# test case 입력 받기
T = int(input())

# test case 수만큼 반복
for _ in range(T):
    # m = 가로, x축 
    # n = 세로, y축
    # k = 양배추 수 
    m, n, k = map(int, input().split())

    cabbages = [[0] * m for _ in range(n)]
    visited = [[True] * m for _ in range(n)]
    count = 0

    for _ in range(k):
        # x, y 입력받음 -> 행에 입력할 때는 [y][x]로 해야 함!! 주의!!
        x, y = map(int, input().split())
        cabbages[y][x] = 1
        visited[y][x] = False

    # i = 세로 j = 가로
    for i in range(n):
        for j in range(m):
            if visited[i][j] == False and cabbages[i][j] == 1:
                count += 1
                visited[i][j] = True
                dfs(i, j, n, m, cabbages, visited)

    print(count)