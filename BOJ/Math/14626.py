import sys

input = sys.stdin.readline

in_str = input().strip()
in_list = list(in_str)
weight = [1, 3] * 7

total_sum = 0
unknown_location = -1

for i in range(13):
    if in_list[i] == '*':
        unknown_location = i
    else:
        total_sum += weight[i] * int(in_list[i])

for unknown_num in range(10):
    check_sum = total_sum + unknown_num * weight[unknown_location]

    if check_sum % 10 == 0:
        print(unknown_num)
        break