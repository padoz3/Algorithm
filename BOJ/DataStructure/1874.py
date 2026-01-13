import sys

input = sys.stdin.readline

n = int(input())
stack = []
print_list = []
top = 1
is_possible = True

for _ in range(n):
    target = int(input())

    # target 숫자가 될 때까지 stack에 숫자 넣기
    while target >= top:
        stack.append(top)
        print_list.append('+')
        top += 1
    
    # target 숫자가 된 경우, stack에서 pop
    if target == stack[-1]:
        stack.pop()
        print_list.append('-')
    else:
        is_possible = False
        break

if is_possible == True:
    for i in print_list:
        print(i)
else:
    print("NO")