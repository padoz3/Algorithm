import sys

input = sys.stdin.readline

T = int(input())

def program(n, m):
    cnt = 0
    for a in range(1, n):
        for b in range(a + 1, n):
            k = (a ** 2 + b ** 2 + m) / (a * b)
            if k == int(k):
                cnt += 1
    return(cnt)


for _ in range(T):
    n, m = map(int, input().split())
    print(program(n, m))
