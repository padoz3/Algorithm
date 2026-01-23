import sys

input = sys.stdin.readline

N = int(input())
input_list = []
num_list = [i for i in range(9, -1, -1)]

alphabet_dict = {}
cnt = 0
sum = 0

ans_dict = {}

for _ in range(N):
    x = input().strip()
    input_list.append(x)
    x_len = len(x)
    for k in list(x):
        if k in alphabet_dict.keys():
            alphabet_dict[k] += 10 ** (x_len - 1)
        else:
            alphabet_dict[k] = 10 ** (x_len - 1)
        x_len -= 1

alphabet_dict = sorted(alphabet_dict.items(), key=lambda x: -x[1])

key_list = [i[0] for i in alphabet_dict]

for x in key_list:
    ans_dict[x] = num_list[cnt]
    cnt += 1

for char, weight in alphabet_dict:
    sum += weight * ans_dict[char]

print(sum)