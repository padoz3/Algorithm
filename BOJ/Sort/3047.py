import sys

input = sys.stdin.readline

nums = list(map(int, input().split()))
nums.sort()

order = list(input().strip())

for i in range(3):
    print(nums[ord(order[i])-65], end=' ')
