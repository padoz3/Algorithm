import sys

input = sys.stdin.readline

n = int(input())
triangle_list = []
for _ in range(n):
    triangle_list.append(list(map(int, input().split())))

ans_list = [[0] * (n+2) for _ in range(n + 2)] 

ans_list[0] = triangle_list[0]

for i in range(1, n):
    for j in range(i + 1):
        if j == 0:
            ans_list[i][j] = ans_list[i-1][j] + triangle_list[i][j]
        elif j == i:
            ans_list[i][j] = ans_list[i-1][j-1] + triangle_list[i][j]
        else:
            ans_list[i][j] += max(ans_list[i-1][j-1] + triangle_list[i][j], 
                                    ans_list[i-1][j] + triangle_list[i][j])

print(max(ans_list[n-1]))