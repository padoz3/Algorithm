import sys

input = sys.stdin.readline

N = int(input())

join_list = []

for _ in range(N):
    age, name = input().split()
    join_list.append([int(age), name])

join_list.sort(key=lambda x: (x[0]))

for member in join_list:
    print(member[0], member[1])