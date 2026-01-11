import sys
from collections import deque 

input = sys.stdin.readline

N = int(input())

num_queue = deque(i for i in range (1, N+1))

while(len(num_queue) != 1):
    num_queue.popleft()
    first = num_queue.popleft()
    num_queue.append(first)


print(f'{num_queue[0]}')