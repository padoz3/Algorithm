import sys

input = sys.stdin.readline

N = int(input())

# 1. 일단 5로 나눠보기
N_5 = N // 5
N_5_rest = N % 5

while(N_5 > 0):
    if N_5_rest % 3 == 0:
        N_3 = N_5_rest // 3
        print(N_3 + N_5)
        break
    if N_5 == 1:
        N_5 = 0
        break
    else:
        N_5 -= 1
        N_5_rest += 5

# 2. N을 5로 나눌 수 없지만 3으로는 나눌 수 있는 경우 경우
if N_5 == 0:
    if N % 3 == 0:
        print(N // 3)
    else:
        print('-1')