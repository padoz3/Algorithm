import sys
import itertools

input = sys.stdin.readline

N, K = map(int, input().split())

N_len = len(str(N))

elements = list(map(int, input().split()))
ans = 0
permut = []

for i in range(N_len, 0, -1):
    permut.extend(list(itertools.product(elements, repeat=i)))

    for p in itertools.product(elements, repeat=i):
        num = int(''.join(map(str, p)))

        if num <= N:
            ans = max(ans, num)
    if ans > 0:
        break

print(ans)