import sys
from collections import deque

input = sys.stdin.readline

# n = 정점의 개수, m = 간선의 개수
n, m = map(int, input().split())
adj = [[] for _ in range(n)]

# 그래프 정보 입력 받기
for _ in range(m):
    u, v = map(int, input().split())
    adj[u].append(v)
    adj[v].append(u)

# 인접리스트 오름차순 정렬
for i in range(n):
    adj[i].sort()

visited = [False] * n

def dfs(v):
    visited[v] = True

    print(v, end=' ')

    for next_node in adj[v]:
        if not visited[next_node]:
            dfs(next_node)

dfs(0)