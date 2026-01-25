import sys
from collections import Counter

input = sys.stdin.readline

num_list = list(map(int, input().split()))

num_list.sort()

curr = num_list[0]

while(True):
    cnt = 0

    for x in num_list:
        if curr % x == 0:
            cnt += 1
    if cnt >= 3:
        print(curr)
        break

    curr += 1