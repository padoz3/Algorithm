import sys

input = sys.stdin.readline

N, M = map(int, input().split())

baskets = [[i, i] for i in range(N+1)]

for i in range(M):
    a, b = map(int, input().split())

    baskets[a][1], baskets[b][1] = baskets[b][1], baskets[a][1]

for j in range(1, N+1):
    print(baskets[j][1], end=' ')
print()