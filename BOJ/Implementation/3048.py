import sys

input = sys.stdin.readline

group_1_len, group_2_len = map(int, input().split())

group_1 = list(input().strip())
group_1.reverse()
group_2 = list(input().strip())
time = int(input())
curr_time = 0

ans = group_1 + group_2
ans_len = group_1_len + group_2_len


for curr_time in range(time):
    # print(curr_time)
    i = 0
    while i < ans_len - 1:
        if ans[i] in group_1 and ans[i+1] in group_2:
            # print(ans)
            ans[i], ans[i+1] = ans[i+1], ans[i]
            i += 2
            # print(ans)
        else:
            i += 1
    # for a in ans:
    #     print(a, end='')
    # print()

for a in ans:
    print(a, end='')