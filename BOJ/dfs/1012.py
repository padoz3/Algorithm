import sys

input = sys.stdin.readline

dy = [+1, -1, 0, 0]
dx = [0, 0, -1, +1]

T = int(input())

def dfs(x, y, M, N, visited, cabbage_layout):
    stack = [(y, x)]
    visited[y][x] = True

    while stack:
        curr_y, curr_x = stack.pop()

        for i in range(4):
            nx = curr_x + dx[i]
            ny = curr_y + dy[i]

            if 0 <= nx < M and 0 <= ny < N: 
                if not visited[ny][nx] and cabbage_layout[ny][nx] == '1':
                    stack.append((ny, nx))
                    visited[ny][nx] = True


for _ in range(T):
    # '1'. 입력 받기
    M, N, K = map(int, input().split())
    cabbage_layout = [['0'] * (M + 1) for _ in range(N + 1)]
    visited =[[False] * (M+1) for _ in range(N+1)]
    cnt = 0

    for i in range(K):
        x, y = map(int, input().split())
        cabbage_layout[y][x] = '1'

    # 2. 근처 배추 찾기
    for i in range(N):
        for j in range(M):
            if cabbage_layout[i][j] == '1' and not visited[i][j]:
                dfs(j, i, M, N, visited, cabbage_layout)
                cnt += 1
    print(cnt)
