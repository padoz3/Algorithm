import sys

input = sys.stdin.readline

T = int(input())

def find_cycle(graph, root, visited):
    node = graph[root]

    while visited[node] == False:
        visited[node] = True
        node = graph[node]

for _ in range(T):
    N = int(input())
    sequence_list = [0]
    input_list = list(map(int, input().split()))
    sequence_list.extend(input_list)
    cnt = 0

    visited = [False] * (N + 1)

    for x in range(1, N + 1):
        if not visited[x]:
            find_cycle(sequence_list, x, visited)
            cnt += 1
    print(cnt)