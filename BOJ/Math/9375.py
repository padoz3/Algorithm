import sys
from collections import Counter

input = sys.stdin.readline

T = int(input())
for _ in range(T):
    category_list = []
    n = int(input())
    answer = 1
    for _ in range(n):
        costume_name, costume_category = input().split()
        category_list.append(costume_category)

    counts = Counter(category_list)
    
    category_counter = counts.values()

    for x in category_counter:
        answer *= (x + 1)
    
    answer -= 1
    print(answer)