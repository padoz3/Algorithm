import sys
from collections import deque

input = sys.stdin.readline

x = int(input())
queue = deque([(x, 0)])
visited = [False] * (x+1)
visited[x] = True

while queue:
    x, count = queue.popleft()

    if x == 1:
        print(count)
        break
    
    if x % 3 == 0 and not visited[x // 3]:
        a = x // 3
        visited[a] = True
        queue.append((a, count + 1))

    if x % 2 == 0 and not visited[x // 2]:
        a = x // 2
        visited[a] = True
        queue.append((a, count + 1))
    if x - 1 >= 1 and not visited[x-1]:
        a = x - 1
        visited[a] = True
        queue.append((a, count + 1))
