import sys

input = sys.stdin.readline

N, M = map(int, input().split())

# 숫자가 입력되는 문제는 리스트를 이용하여 찾음
pokemon_list = []

# 이름이 입력되는 문제는 딕셔너리를 이용하여 찾음
pokemon_dict = {}
index = 1

for _ in range(N):
    pokemon_name = input().rstrip()
    pokemon_list.append(pokemon_name)

    pokemon_dict[pokemon_name] = index
    index += 1

for _ in range(M):
    a = input().rstrip()

    # 숫자가 입력된 경우, 리스트를 이용해서 찾음
    if a.isdecimal() == True:
        print(pokemon_list[int(a) - 1])
    else:
    # 이름이 입력된 경우, 딕셔너리를 이용해서 찾음
        print(pokemon_dict[a])