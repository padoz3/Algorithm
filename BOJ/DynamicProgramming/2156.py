import sys

input = sys.stdin.readline

n = int(input())
wine_list = [0]
hyojoo_wine = [0] * 10001

for _ in range(n):
    wine_list.append(int(input()))

if n >= 1:
    hyojoo_wine[1] = wine_list[1]
if n >= 2:
    hyojoo_wine[2] = wine_list[1] + wine_list[2]
if n >= 3:
    for i in range(3, n + 1):
        hyojoo_wine[i] = max(hyojoo_wine[i-2] + wine_list[i], 
                             hyojoo_wine[i-3] + wine_list[i-1] + wine_list[i],
                             hyojoo_wine[i-1])
print(max(hyojoo_wine))