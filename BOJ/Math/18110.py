import sys
from statistics import mean

input = sys.stdin.readline

def round_half_up(num):
    return int(num + 0.5)

N = int(input())

if N == 0:
    print(0)
else:
    level_list = []

    for i in range(N):
        level_list.append(int(input()))

    remove = round_half_up(N * 0.15)

    level_list.sort()

    if remove > 0:
        trimmed_list = level_list[remove: N - remove]
    else:
        trimmed_list = level_list

    if not trimmed_list:
        print(0)
    else:
        avg = round_half_up(mean(trimmed_list))
        print(avg)