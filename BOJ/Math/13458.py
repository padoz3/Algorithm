import sys

input = sys.stdin.readline

N = int(input())
candidate = list(map(int, input().split()))
B, C = map(int, input().split())

count = 0

for i in range(N):
    a = candidate[i] - B
    if a <= 0:
        count += 1
    else:
        b = a // C
        rest = a % C
        if rest > 0:
            count += b + 2
        else:
            count += b + 1

print(count)