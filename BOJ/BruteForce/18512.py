import sys

input = sys.stdin.readline

x, y, orin_p1, orin_p2 = map(int, input().split())
p1 = orin_p1
p2 = orin_p2

while(p1 <= orin_p1 + x * y or p2 <= orin_p2 + x * y):
    if p1 > p2:
        p2 += y
    if p1 < p2:
        p1 += x
    if p1 == p2:
        print(p1)
        sys.exit()

print(-1)