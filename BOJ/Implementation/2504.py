import sys
from collections import deque

input = sys.stdin.readline

strings = list(input().strip())
stack = deque([])
rst = []

len_strings = len(strings)
idx = 0
ans = 0
is_error = False

def little_parenthesis(idx, stn):
    total = 0
    while idx < len(stn):
        if stn[idx] == '(':
            next_idx, value = little_parenthesis(idx+1, stn)
            if value == -1: 
                return -1, -1
            total += value
            idx = next_idx
        elif stn[idx] == '[':
            next_idx, value = big_parenthesis(idx+1, stn)
            if value == -1: 
                return -1, -1
            total += value
            idx = next_idx
        elif stn[idx] == ')':
            if total == 0:
                total = 2
            else:
                total *= 2
            return idx + 1, total
        else:
            return -1, -1
    return -1, -1

def big_parenthesis(idx, stn):
    total = 0
    while idx < len(stn):
        if stn[idx] == '(':
            next_idx, value = little_parenthesis(idx+1, stn)
            if value == -1: 
                return -1, -1
            total += value
            idx = next_idx
        elif stn[idx] == '[':
            next_idx, value = big_parenthesis(idx+1, stn)
            if value == -1: 
                return -1, -1
            total += value
            idx = next_idx
        elif stn[idx] == ']':
            if total == 0:
                total = 3
            else:
                total *= 3
            return idx + 1, total
        else:
            return -1, -1
    return -1, -1


while idx < len_strings:
    curr = 0
    if strings[idx] == '(':
        idx, curr = little_parenthesis(idx+1, strings)
        if curr == -1:
            is_error = True
            break
        ans += curr
    elif strings[idx] == '[':
        idx, curr = big_parenthesis(idx+1, strings)
        if curr == -1:
            is_error = True
            break
        ans += curr
    else:
        is_error = True
        break
        
    
if is_error:
    print(0)
else:
    print(ans)