import sys

input = sys.stdin.readline

# 3을 표현하는 방법 = 4가지
# 1. 3
# 2. 1+2
# 3. 2+1
# 4. 1+1+1

# 2를 표현하는 방법 = 2가지
# 1. 2
# 2. 1+1

# 1을 표현하는 방법 = 1가지. 
# 1. 1

number_cases = [0]
number_cases.append(1)
number_cases.append(2)
number_cases.append(4)


target_list = []
T = int(input())

for _ in range(T):
    target_list.append(int(input()))

max_num = max(target_list)

for i in range(4, max_num + 1):
    number_cases.append(number_cases[i-1]+number_cases[i-2]+number_cases[i-3])

for idx in target_list:
    print(number_cases[idx])