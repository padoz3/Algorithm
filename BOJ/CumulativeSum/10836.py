import sys

input = sys.stdin.readline

m, n = map(int, input().split())
growth_list = []
for i in range(n):
    growth_list.append(list(map(int, input().split())))

larva = [[1] * m for _ in range(m)]
diff = [0] * (2 * m - 1)

for i in range(n):
    a = growth_list[i][0]
    b = growth_list[i][1]

    if a < 2 * m - 1:
        diff[a] += 1
    if a + b < 2 * m - 1:
        diff[a+b] += 1

cum_gth = 0
final_gth = [0] * (2 * m - 1)

for i in range(2 * m - 1):
    cum_gth += diff[i]
    final_gth[i] = cum_gth

idx = 0
for i in range(m-1, -1, -1):
    larva[i][0] += final_gth[idx]
    idx += 1
for i in range(1, m):
    larva[0][i] += final_gth[idx]
    idx += 1

for i in range(1, m):
    for j in range(1, m):
        larva[i][j] = larva[i-1][j]

for i in range(m):
    for j in range(m):
        print(larva[i][j], end=' ')
    print('')