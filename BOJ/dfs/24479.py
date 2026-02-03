import sys

input = sys.stdin.readline

N, M, R = map(int, input().split())

graph = [[] for i in range((N + 1))]

for _ in range(M):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)

for j in range(N + 1):
    graph[j].sort()

def dfs_stack(root, graph):
    visited = [False] * (N + 1)
    stack = [root]

    order = [0] * (N + 1)
    cnt = 0

    while stack:
        node = stack.pop()

        if not visited[node]:
            visited[node] = True
            cnt += 1
            order[node] = cnt

            for neighbor in reversed(graph[node]):
                if not visited[neighbor]:
                    stack.append(neighbor)

    return order

ans = dfs_stack(R, graph)

for i in range(1, N + 1):
    print(ans[i])