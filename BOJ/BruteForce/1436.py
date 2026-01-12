import sys

input = sys.stdin.readline

N = int(input())

# 6이 적어도 3개 이상 연속으로 들어가는 수를 연속으로 만 개 구해야 함!!

num = 666
title_list = []
iterator = 0

while(1):
    if '666' in str(num):
        title_list.append(num)
        iterator += 1
        if iterator == N:
            print(num)
            break
        num += 1
    else:
        num += 1