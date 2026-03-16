import sys

input = sys.stdin.readline

stair_count = int(input())
stairs = []
scores = [0] * 301

for _ in range(stair_count):
    stairs.append(int(input()))

if stair_count >= 1:
    scores[0] = stairs[0]
if stair_count >= 2:
    scores[1] = stairs[0] + stairs[1]
if stair_count >= 3:
    for i in range(2, stair_count):
        scores[i] = max(scores[i - 2] + stairs[i], scores[i - 3] + stairs[i-1] + stairs[i])
        
print(scores[stair_count - 1])