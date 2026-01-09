import sys
from collections import deque

input = sys.stdin.readline

N, K = map(int, input().split())

num_queue = deque(i for i in range(1, N+1))
print('<', end='')

while len(num_queue) > 1:
    num_queue.rotate(-K+1)
    print(num_queue.popleft(), end=', ')

print(num_queue.popleft(), end='')
print('>')