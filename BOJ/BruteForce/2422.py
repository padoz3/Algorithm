import sys
from itertools import combinations

input = sys.stdin.readline

N, M = map(int, input().split())

banned_set = set()

for _ in range(M):
    a, b = input().split()
    banned_set.add((a, b))
    banned_set.add((b, a))

candidates = combinations([str(i) for i in range(1, N + 1)], 3)
cnt = 0

for a, b, c in candidates:
    if (a, b) in banned_set or (b, c) in banned_set or (a, c) in banned_set:
        continue
    else:
        cnt += 1

print(cnt)
