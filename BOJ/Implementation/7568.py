import sys

N = int(input())

people_list = []
rank = 1
rank_list = []

for _ in range(N):
    people_list.append(list(map(int, input().split())))

for i in range(N):
    rank = 1
    iterator = 0
    for iterator in range(N):
        if people_list[iterator][0] > people_list[i][0]: 
            # 누군가 나보다 몸무게가 더 많이 나가는 경우, 키도 더 큰지 확인
            if people_list[iterator][1] > people_list[i][1]:
                # 키도 더 크다면 그 사람은 나보다 덩치가 더 큰 것
                rank += 1
            # 그렇지 않다면, 그 사람은 나와 덩치가 같은 것.

    rank_list.append(rank)

for i in range(N):
    print(rank_list[i], end=' ')