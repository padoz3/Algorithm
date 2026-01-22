import sys

input = sys.stdin.readline

N, K = map(int, input().split())

count = 0

hrs = [i for i in range(N + 1)]
mins = [i for i in range(60)]

K = str(K)

for h in hrs:
    for m in mins:
        for s in mins:
            time_str = f"{h:02}{m:02}{s:02}"
            if K in time_str:
                count += 1
print(count)