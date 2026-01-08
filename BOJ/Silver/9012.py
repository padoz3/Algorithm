import sys

input = sys.stdin.readline

N = int(input())

for i in range(N):
    input_string = input().strip()
    stack = []

    for j in input_string:
        if j == '(':
            stack.append('(')
        elif j == ')':
            if len(stack) == 0:
                stack.append(')')
                break
            else:
                stack.pop()

    if len(stack) != 0:
        print("NO")
    else:
        print("YES")
