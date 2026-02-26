import sys

input = sys.stdin.readline

# 나라 별 메달 수가 두 개 이하 

N = int(input().strip())
students = []
countries = []
ans = []

for i in range(N):
    country, student_num, score = map(int, input().split())
    students.append([country, student_num, score])

students.sort(key=lambda x:(-x[2]))

idx = 0

while idx < N and len(ans) <= 3:
    country, student_num, score = students[idx][0], students[idx][1], students[idx][2]
    
    if countries.count(country) < 2:
        ans.append([country, student_num, score])
        countries.append(country)
    idx += 1

for i in range(3):
    print(ans[i][0], ans[i][1])