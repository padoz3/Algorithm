import sys

input = sys.stdin.readline

n = int(input())
a, b = map(int, input().split())
m = int(input())

graph = [[] for _ in range (n + 1)]

for _ in range(m):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)

def dfs_stack(start_node):
    visited = [False] * (n + 1)
    stack = [(start_node, 0)]

    while stack:
        node, dist = stack.pop()
        if node == b:
            return(dist)

        if not visited[node]:
            visited[node] = True
            dist += 1
            for neighbor in reversed(graph[node]):
                if not visited[neighbor]:
                    stack.append((neighbor, dist))
    return(-1)

result = dfs_stack(a)
print(result)