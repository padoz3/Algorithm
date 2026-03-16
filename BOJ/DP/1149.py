import sys

input = sys.stdin.readline

N = int(input())
cost_list = [[0, 0, 0]] * 10001

ans_list = [[0] * 3 for _ in range(10001)]

r = 0
g = 1
b = 2

for i in range(1, N + 1):    
    cost_list[i] = list(map(int, input().split()))

ans_list[1] = cost_list[1]

for i in range(2, N + 1):
    red = min(ans_list[i-1][g] + cost_list[i][r], ans_list[i-1][b] + cost_list[i][r])
    green = min(ans_list[i-1][r] + cost_list[i][g], ans_list[i-1][b] + cost_list[i][g])
    blue = min(ans_list[i-1][r] + cost_list[i][b], ans_list[i-1][g] + cost_list[i][b])
    
    ans_list[i] = [red, green, blue]

print(min(ans_list[N]))