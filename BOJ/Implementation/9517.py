import sys
from collections import deque

input = sys.stdin.readline

# 게임이 시작했을 때 폭탄을 들고 있는 사람 번호
k = int(input())

players = deque([i for i in range(1, 9)])
while players[0] != k:
    players.rotate(1)

# 질문의 개수
n = int(input())

bomb_time = 3 * 60 + 30
curr_time = 0

for i in range(n):
    a, b = input().split()
    
    curr_time += int(a)

    if curr_time >= bomb_time:
        break

    # 문제의 정답을 맞춘 경우에는 폭탄을 바로 왼쪽에 있는 플레이어에게 넘겨주고, 
    # 넘겨받은 플레이어에게 다음 질문이 나가게 된다.
    if b == 'T':
        players.rotate(-1)

print(players[0])