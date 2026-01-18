import sys

input = sys.stdin.readline

N, M = map(int, input().split())

maze = []

ans_list = [[0] * (M) for _ in range(N)]

for i in range(N):
    maze.append(list(map(int, input().split())))

ans_list[0][0] = maze[0][0]

for j in range(1, M):
    ans_list[0][j] = ans_list[0][j - 1] + maze[0][j]

for i in range(1, N):
    for j in range(M):
        if j == 0:
            ans_list[i][j] = maze[i][j] + ans_list[i-1][j]
        else:
            ans_list[i][j] = maze[i][j] + max(ans_list[i-1][j-1], 
                                              ans_list[i-1][j],
                                              ans_list[i][j-1])
        
print(ans_list[N-1][M-1])