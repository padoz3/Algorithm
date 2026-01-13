import sys

input = sys.stdin.readline

sentence_list = []

# 몇 줄이 입력될 지 모르는 경우 
# 일단 입력 받기
while True:
    A = input()
    if A[0] == '.':
        break
    else:
        A_list = list(A)
        sentence_list.append(A_list)

for sentence in sentence_list:
    sentence_len = len(sentence)
    stack = []
    for i in range(sentence_len):
        if sentence[i] == '[':
            stack.append('[')
        elif sentence[i] == ']':
            if len(stack) > 0 and stack[-1] == '[':
                stack.pop()
            else:
                print("no")
                break
        elif sentence[i] == '(':
            stack.append('(')
        elif sentence[i] == ')':
            if len(stack) > 0 and stack[-1] == '(':
                stack.pop()
            else:
                print("no")
                break
        elif sentence[i] == '.':
            if len(stack) == 0:
                print("yes")
            else:
                print("no")
            break