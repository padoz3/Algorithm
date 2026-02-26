import sys

input = sys.stdin.readline

nums = [i for i in range(1, 21)]

for i in range(10):
    a, b = map(int, input().split())
    a -= 1

    change_nums = nums[a:b]
    change_nums.reverse()
    
    for j in range(a, b):
        nums[j] = change_nums[j-a]
    

for i in range(20):
    print(nums[i], end = ' ')
print()