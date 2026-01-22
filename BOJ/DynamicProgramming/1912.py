import sys

input = sys.stdin.readline

n = int(input())

num_list = list(map(int, input().split()))

sum = num_list[0]
dp = [0 for _ in range(n)]

max_loc = 0

for i in range(1, n):
    num_list[i] = max(num_list[i], num_list[i-1] + num_list[i])
    print(i, num_list[i])

print(max(num_list))