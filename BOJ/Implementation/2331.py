import sys
from collections import Counter

input = sys.stdin.readline

A, P = map(int, input().split())

sequence_list = [A]
repeat_list = []

for i in range(1, 100000):
    target = str(sequence_list[i - 1])
    tar_len = len(target)
    curr = 0
    for j in range(tar_len):
        curr += int(target[j]) ** P
    sequence_list.append(curr)

counts = Counter(sequence_list)

result = [x for x in sequence_list if counts[x] == 1]

print(len(result))