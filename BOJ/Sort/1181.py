import sys

input = sys.stdin.readline

N = int(input())

word_list = []

for _ in range(N):
    word_list.append(input().strip())

# 중복 제거
word_list = list(set(word_list))

# 길이순 - 사전순 정렬
word_list.sort(key=lambda x: (len(x), x))

for word in word_list:
    print(word)