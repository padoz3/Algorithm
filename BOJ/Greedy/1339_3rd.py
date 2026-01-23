import sys

input = sys.stdin.readline

N = int(input())

alphabet_dict = {}
sum_val = 0
num_idx = 0
num_list = [i for i in range(9, -1, -1)]

# 1. 가중치 계산
for _ in range(N):
    x = input().strip()
    x_len = len(x)
    for k in list(x):
        if k in alphabet_dict.keys():
            alphabet_dict[k] += 10 ** (x_len - 1)
        else:
            alphabet_dict[k] = 10 ** (x_len - 1)
        x_len -= 1

# 2. 정렬 - 리스트로 변환됨
sorted_list = sorted(alphabet_dict.items(), key=lambda x: -x[1])

# 3. 계산
for char, weight in sorted_list:
    sum_val += weight * num_list[num_idx]
    num_idx += 1

print(sum_val)