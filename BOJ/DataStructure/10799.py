import sys
from collections import deque

input = sys.stdin.readline

parenthesis = list(input())
len_parenthesis = len(parenthesis)
stack = deque([])
ans = 0

cnt = 0
idx = 0

while idx < len_parenthesis:
    # 레이저가 입력된 경우
    if parenthesis[idx] == '(' and idx + 1 < len_parenthesis and parenthesis[idx+1] == ')':
        ans += len(stack)
        cnt += 1
        idx += 1
    # 여는 괄호 입력된 경우
    elif parenthesis[idx] == '(':
        stack.append('(')
    # 닫는 괄호 입력된 경우
    elif parenthesis[idx] == ')':
        if len(stack) > 0:
            stack.pop()
        ans += 1
    idx += 1

print(ans)