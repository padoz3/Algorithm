import sys

input = sys.stdin.readline

N = int(input())
dot_list = []

for i in range(N):
    x = list(map(int, input().split()))
    dot_list.append(x)

dot_list = sorted(dot_list, key = lambda x : (x[1], x[0]))

for i in range(N):
    print(dot_list[i][0], dot_list[i][1])