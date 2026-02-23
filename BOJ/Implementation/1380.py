import sys

input = sys.stdin.readline

n = int(input())
ans_list = []
test_case = 1

while n != 0:
    students = []
    # earrings = {}
    earrings = []

    for i in range(n):
        students.append(input().strip())
    
    for i in range(2*n-1):
        num, al = input().split()

        if num in earrings:
            earrings.remove(num)
        else:
            # earrings[num] = al
            earrings.append(num)

    ans = earrings.pop() 
    ans = int(ans)

    ans_list.append([test_case, students[ans-1]])

    test_case += 1
    n = int(input())

ans_len = len(ans_list)

for i in range(ans_len):
    print(ans_list[i][0], ans_list[i][1])