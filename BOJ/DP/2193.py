import sys

input = sys.stdin.readline

n = int(input())
pin_nums = [0] * 91
pin_nums[1], pin_nums[2] = 1, 1

for i in range(3, n + 1):
    pin_nums[i] = pin_nums[i - 1] + pin_nums[i - 2]

print(pin_nums[n])