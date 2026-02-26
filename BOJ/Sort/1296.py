import sys

input = sys.stdin.readline

name = input().strip()
yeon_name = list(name)
len_name = len(name)

N = int(input())
team_names = []

for i in range(N):
    team_name = input().strip()
    t_name = team_name + name

    L = t_name.count('L')
    O = t_name.count('O')
    V = t_name.count('V')
    E = t_name.count('E')

    ans = ((L+O) * (L+V) * (L+E) * (O+V) * (O+E) * (V+E)) % 100

    team_names.append([team_name, ans])

team_names.sort(key=lambda x: (-x[1], x[0]))

print(team_names[0][0])