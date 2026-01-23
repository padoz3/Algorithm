import sys
from itertools import permutations

input = sys.stdin.readline

N = int(input())

if N == 1:
    print(1)
elif N == 2:
    print(1, 2)
    print(2, 1)
else:
    candidates = list(permutations([str(i) for i in range(1, N + 1)], ))

    for row in candidates:
        print(*row)