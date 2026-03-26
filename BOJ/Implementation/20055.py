import sys
from collections import deque

N, K = map(int, input().split())
arrays = deque(list(map(int, input().split())))
robots = deque(list([0] * N))

stage_count = 0

while 1:
    # stage 1. 벨트가 각 칸 위에 있는 로봇과 함께 한 칸 회전한다.
    stage_count += 1
    arrays.rotate(1)
    robots.rotate(1)

    # stage 1-1. N번째에 있는 로봇 내리기
    if robots[N-1] == 1:
        robots[N-1] = 0

    # stage 2. 가장 먼저 벨트에 올라간 로봇부터, 
    # 벨트가 회전하는 방향으로 한 칸 이동할 수 있다면 이동한다. 
    # 만약 이동할 수 없다면 가만히 있는다.
    for i in range(N-2, -1, -1):
        # i번째에 로봇이 있고, 그 다음칸엔 로봇이 없으며
        if robots[i] == 1 and robots[i+1] == 0:
            # 다음 벨트의 내구성이 1 이상이라면
            if arrays[i+1] > 0:
                # 로봇 이동시키기
                robots[i] = 0
                robots[i+1] = 1

                # 다음칸 내구성 -= 1
                arrays[i+1] -= 1
    if robots[N-1] == 1:
        robots[N-1] = 0

    # stage 3. 올리는 위치에 있는 칸의 내구도가 0이 아니면 
    # 올리는 위치에 로봇을 올린다.
    if arrays[0] > 0:
        arrays[0] -= 1
        robots[0] = 1

    # stage 4.내구도가 0인 칸의 개수가 K개 이상이라면 과정을 종료한다. 
    # 그렇지 않다면 1번으로 돌아간다.
    zero_count = arrays.count(0)
    if zero_count >= K:
        break

print(stage_count)