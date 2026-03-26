import sys
from collections import deque
from math import floor
input = sys.stdin.readline
dx = [0, 1, 1, 1, 0, -1, -1, -1]
dy = [-1, -1, 0, 1, 1, 1, 0, -1]
# N*N 행렬, 파이어볼 M개, 파이어볼 K번 이동
N, M, K = map(int, input().split())
fireballs = [[[] for _ in range(N)] for _ in range(N)]

# 맨 처음, 파이어볼 정보 입력받기
for _ in range(M):
    # 위치: [행, 열], 질량, 속력, 방향
    r, c, m, s, d = map(int, input().split())
    fireballs[r-1][c-1].append([m, s, d])

# 명령!!
for count in range(K):
    # print("count", count)
    new_fireballs = [[[] for _ in range(N)] for _ in range(N)]
    # 모든 파이어볼 이동
    for i in range(N):
        for j in range(N):
            if len(fireballs[i][j]) > 0:
                # print("이동 전", i, j, "에 있는 파이어볼 개수", len(fireballs[i][j]))
                for k in range(len(fireballs[i][j])):
                    m, s, d = fireballs[i][j][k]
                    r = (i + dy[d] * s) % N
                    c = (j + dx[d] * s) % N
                    new_fireballs[r][c].append([m, s, d])
                    # print("이동전", i, j, m, s, d, "이동후", r, c)
    
    # 이동이 모두 끝난 뒤 질량 계산
    for i in range(N):
        for j in range(N):
            # 합쳐야 하는 경우
            if len(new_fireballs[i][j]) > 1:
                new_mass = 0
                new_speed = 0
                new_dir = 0

                for k in range(len(new_fireballs[i][j])):
                    # print("합쳐져야함",new_fireballs[i][j])
                    new_mass += new_fireballs[i][j][k][0]
                    new_speed += new_fireballs[i][j][k][1]

                is_even = new_fireballs[i][j][0][2] % 2
                is_same = True
                for k in range(1, len(new_fireballs[i][j])):
                    if new_fireballs[i][j][k][2] % 2 != is_even:
                        is_same = False
                        break
                
                # print("나누기 전", new_mass)
                new_mass //= 5
                # print("나누기 후", new_mass)
                new_speed //= len(new_fireballs[i][j])
                if is_same == True:
                    new_direction = [0, 2, 4, 6]
                else:
                    new_direction = [1, 3, 5, 7]

                new_fireballs[i][j] = []

                # 질량 0인 경우 소멸
                if new_mass > 0:
                    for k in range(4):
                        new_fireballs[i][j].append([new_mass, new_speed, new_direction[k]])

    fireballs = new_fireballs

total_mass = 0
for i in range(N):
    for j in range(N):
        if len(fireballs[i][j]) > 0:
            for k in range(len(fireballs[i][j])):
                total_mass += fireballs[i][j][k][0]

print(total_mass)