import sys

input = sys.stdin.readline

N, M = map(int, input().split())
pw_dict = {}

for _ in range(N):
    website, pw = input().split()
    pw_dict[website] = pw

for _ in range(M):
    target = input().rstrip()
    print(pw_dict[target])