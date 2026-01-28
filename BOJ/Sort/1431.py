import sys
from collections import Counter

input = sys.stdin.readline

def get_sum(serial):
    result = 0
    for char in serial:
        if char.isdigit(): # 만약 해당 char 이 숫자라면
            result += int(char)
    return result

N = int(input())

serial_list = []

for _ in range(N):
    serial_list.append(input().strip())

serial_list.sort(key=lambda x: (len(x), get_sum(x), x))

for x in serial_list:
    print(x)