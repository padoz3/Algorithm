import sys

input = sys.stdin.readline

N, M = map(int, input().split())
board = []
modify = []

for i in range(N):
    board.append(input().strip())

for i in range(N - 7):
    for j in range(M - 7):
        modify_W = 0 # 시작점이 W일 때 수정해야 하는 칸 개수
        modify_B = 0 # 시작점이 B일 때 수정해야 하는 칸 개수

        for x in range(i, i + 8):
            for y in range(j, j + 8):
                if (x + y) % 2 == 0:
                    # 시작점과 색이 같아야 함
                    if board[x][y] == 'B': modify_W += 1
                    if board[x][y] == 'W': modify_B += 1
                else:
                    # 시작점과 색이 달라야 함
                    if board[x][y] == 'B': modify_B += 1
                    if board[x][y] == 'W': modify_W += 1
                
        modify.append(min(modify_B, modify_W))

print(min(modify))