import sys

input = sys.stdin.readline

# 재현이는 잘못된 수를 부를 때마다 0을 외쳐서, 가장 최근에 재민이가 쓴 수를 지우게 시킨다.
# 재민이는 이렇게 모든 수를 받아 적은 후 그 수의 합을 알고 싶어 한다. 재민이를 도와주자!

K = int(input())
num_list = []

for _ in range(K):
    a = int(input())
    if a == 0:
        num_list.pop()
    else:
        num_list.append(a)

total_sum = sum(num_list)

print(total_sum)