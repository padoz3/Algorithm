import sys
from collections import deque

input = sys.stdin.readline

T = int(input())

for _ in range(T):
    turtles = list(input().strip())
    turtles_len = len(turtles)
    curr_x = curr_y = 0
    weight_x = deque([0, -1, 0, +1])
    weight_y = deque([+1, 0, -1, 0])
    min_x = min_y = max_x = max_y = 0

    for i in range(turtles_len):
        curr = turtles[i]

        if curr == 'F':
            curr_x += weight_x[0]
            curr_y += weight_y[0]
        elif curr == 'B':
            curr_x -= weight_x[0]
            curr_y -= weight_y[0]
        elif curr == 'L':
            weight_x.rotate(-1)
            weight_y.rotate(-1)
        elif curr == 'R':
            weight_x.rotate(1)
            weight_y.rotate(1)

        min_x = min(min_x, curr_x)
        max_x = max(max_x, curr_x)

        min_y = min(min_y, curr_y)
        max_y = max(max_y, curr_y)

    ans = (max_x - min_x) * (max_y - min_y)
    print(ans)