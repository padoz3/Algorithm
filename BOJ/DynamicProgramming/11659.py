import sys

input = sys.stdin.readline

N, M = map(int, input().split())

num_list = list(map(int, input().split()))
sum_list = [0]
sum = 0

for num in num_list:
    sum += num
    sum_list.append(sum)

for _ in range(M):
    start, end = map(int, input().split())
    print(sum_list[end] - sum_list[start - 1])
