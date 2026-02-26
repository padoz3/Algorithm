import sys
from collections import deque

input = sys.stdin.readline

N, K = map(int, input().split())
memos = []
apbs = deque([0] * N)
is_error = False

for i in range(K):
    change, alphabet = input().split()
    change = int(change)
    apbs.rotate(-change)

    if apbs[0] != 0:
        if apbs[0] == alphabet:
            continue
        else:
            is_error = True
            break
    else:
        if apbs[0] == 0:         
            apbs[0] = alphabet
        else:
            is_error = 0
    # print(apbs)

only_alphabets = [x for x in apbs if x != 0]
only_alphabets_set = set(only_alphabets)
if len(only_alphabets) != len(only_alphabets_set):
    is_error = True

apbs.rotate(N)

# print(apbs)
if is_error == True:
    print('!')
else:
    for i in range(N):
        if apbs[0] == 0:
            print('?', end='')
        else:
            print(apbs[0], end='')
        apbs.rotate(1)