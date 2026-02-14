import sys

input = sys.stdin.readline

p, m = map(int, input().split())
rooms_list = []

for i in range(p):
    l, n = input().split()
    l = int(l)
    matched = False

    rooms_len = len(rooms_list)

    # 개설된 방이 아예 없는 경우
    if rooms_len == 0:
        rooms_list.append([l, [(l, n)]])
        matched = True
    else:
        for j in range(rooms_len):
            current_room = rooms_list[j]
            room_lev = current_room[0]
            current_players = current_room[1]

            if room_lev - 10 <= l <= room_lev + 10:
                # 정원 아직 다 안 찬 경우, 현재 플레이어 추가하기
                if len(current_players) < m:
                    rooms_list[j][1].append((l, n))
                    matched = True
                    brea

            # 모든 방을 확인했지만 들어갈 수 있는 방이 없는 경우
        if matched == False:
            rooms_list.append([l, [(l, n)]])

for room in rooms_list:
    player_len = len(room[1])

    if player_len == m:
        print('Started!')
    else:
        print('Waiting!')

    room[1].sort(key=lambda x:x[1])

    for a, b in room[1]:
        print(a, b)