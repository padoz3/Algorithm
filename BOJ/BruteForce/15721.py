import sys

input = sys.stdin.readline

input_list = []
bd_list = [0, 1, 0, 1]

cnt = 0

for _ in range(3):
    input_list.append(int(input()))

A, T, g = input_list[0], input_list[1], input_list[2]

people = 0

for i in range(2, 60 * T):
    curr_list = bd_list + [0] * i + [1] * i
    for c in curr_list:
        if c == g:
            cnt += 1
            if cnt == T:
                print(people)
                sys.exit()
        people += 1
        people %= A
        