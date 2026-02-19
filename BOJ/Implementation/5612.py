import sys

input = sys.stdin.readline

# 조사한 시간 n분
n = int(input())
# 조사를 시작할 때 터널 안에 들어 있는 차량의 수
m = int(input())

car_list = []

max_m = m

for i in range(1, n+1):
    # a, b = map(int, input().split())
    car_list.append(list(map(int, input().split())))

for i in range(n):
    m += car_list[i][0]
    m -= car_list[i][1]

    if m < 0:
        max_m = 0
        break
    
    max_m = max(m, max_m)

print(max_m)