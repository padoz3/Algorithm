import sys

input = sys.stdin.readline

# 컴퓨터 수 입력
n = int(input())

computers = [[] for _ in range(n + 1)]
visited = [False] * (n+1)

# 네트워크 상에서 직접 연결되어있는 컴퓨터 쌍의 수
m = int(input())

# 네트워크상에서 직접 연결되어 있는 컴퓨터의 번호 쌍
for _ in range(m):
    u, v = map(int, input().split())
    computers[u].append(v)
    computers[v].append(u)

def dfs(v):
    visited[v] = True
    global count

    count += 1

    for next_node in computers[v]:
        if not visited[next_node]:
            dfs(next_node)

count = 0
dfs(1)
print(count-1)