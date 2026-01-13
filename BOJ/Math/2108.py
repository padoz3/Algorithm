import sys
from collections import Counter

input = sys.stdin.readline

########################## 함수 정의
# 1. 산술평균
def mean(target_list):
    return round(sum(target_list) / N)

# 2. 중앙값
def median(target_list):
    return target_list[N // 2]

# 3. 최빈값
def mode(target_list):
    mode_count = Counter(target_list).most_common()
    # print(mode_count)
    # 최빈값 2개 이상인 경우, 2번째로 작은 수 반환
    if len(mode_count) > 1 and mode_count[0][1] == mode_count[1][1]:
        return mode_count[1][0]
    else:
        return mode_count[0][0]

# 4. 범위 출력
def list_range(target_list):
    return target_list[-1] - target_list[0]
########################## 함수 정의

N = int(input())
num_list = []

for _ in range(N):
    num_list.append(int(input()))

num_list.sort()

print(mean(num_list))
print(median(num_list))
print(mode(num_list))
print(list_range(num_list))