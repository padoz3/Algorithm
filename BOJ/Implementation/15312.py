import sys

input = sys.stdin.readline

alphabets = [3, 2, 1, 2, 3, 3, 2, 3, 3, 2, 2, 1, 2, 2, 1, 2, 2, 2, 1, 2, 1, 1, 1, 2, 2, 1]

name_1 = list(input().strip())
name_2 = list(input().strip())

name_len = len(name_1)

ans = []

for i in range(name_len):
    a = ord(name_1[i]) - 65
    b = ord(name_2[i]) - 65

    a_num = alphabets[a]
    b_num = alphabets[b]

    ans.append(a_num)
    ans.append(b_num)

while len(ans) > 2:
    ans_len = len(ans)
    new_ans = []
    for i in range(ans_len - 1):
        a = ans[i]
        b = ans[i + 1]
        new_ans.append((a+b)%10)
    ans = new_ans

for i in range(len(ans)):
    print(ans[i],end="")