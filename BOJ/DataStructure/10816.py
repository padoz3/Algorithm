import sys
from collections import Counter

input = sys.stdin.readline

N = int(input())
sanggeun_list = list(map(int, input().split()))

M = int(input())
cal_list = list(map(int, input().split()))

sanggeun_dict = Counter(sanggeun_list)
# print(sanggeun_dict)

for c in cal_list:
    if c in sanggeun_dict:
        print(sanggeun_dict[c], end=' ')
    else:
        print('0', end=' ')