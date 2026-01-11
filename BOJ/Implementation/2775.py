import sys

input = sys.stdin.readline

T = int(input())
apart_list = []
max_n = -1
max_k = -1

for i in range(T):
    k = int(input())
    n = int(input()) 

    max_k = max(k, max_k)
    max_n = max(n, max_n)

    apart_list.append([k, n])

resident_list = [[0] * (max_n + 1) for i in range(max_k + 1)]
resident_list[0] = [i for i in range (max_n+1)]

for i in range(1, max_k + 1):
    for j in range(max_n + 1):
        resident_list[i][j] = resident_list[i-1][j] + resident_list[i][j-1]

for i in range(T):
    print(resident_list[apart_list[i][0]][apart_list[i][1]])