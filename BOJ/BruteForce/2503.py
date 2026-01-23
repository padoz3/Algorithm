import sys
from itertools import permutations

input = sys.stdin.readline

N = int(input())
test_cases = []
ans = [0] * 3

for _ in range(N):
    num, strike, ball = map(int, input().split())
    test_cases.append([str(num), strike, ball])

ans = 0

candidates = list(permutations([str(i) for i in range(1, 10)], 3))

for num in candidates:
    is_possible = True

    for input_num, input_s, input_b in test_cases:
        strike_cnt = 0
        ball_cnt = 0

        for i in range(3):
            if num[i] == input_num[i]:
                strike_cnt += 1
            elif num[i] in input_num:
                ball_cnt += 1

        if strike_cnt != input_s or ball_cnt != input_b:
            is_possible = False
            break
    if is_possible:
        ans += 1
    
print(ans)