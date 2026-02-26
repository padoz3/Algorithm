import sys

input = sys.stdin.readline

n = int(input().strip())

while n != 0:
    words = []
    for i in range(n):
        word = input().strip()
        words.append([word, word.lower()])
    words.sort(key=lambda x:x[1])
    print(words[0][0])
    n = int(input().strip())