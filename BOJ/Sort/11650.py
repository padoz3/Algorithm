import sys

input = sys.stdin.readline

N = int(input())
dot_list = []

for _ in range(N):
    x, y = map(int, input().split())
    dot_list.append([x, y])

dot_list.sort(key=lambda x: (x[0], x[1]))

for i in range(N):
    print(dot_list[i][0], dot_list[i][1])