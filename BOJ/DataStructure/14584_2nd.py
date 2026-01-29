import sys

input = sys.stdin.readline

code = input().strip()
code_list = list(code)

dictionary = []

N = int(input())

for _ in range(N):
    dictionary.append(input().strip())

for i in range(26):
    ans = ""
    for char in code_list:
        ans += chr((ord(char) - 97 + i) % 26 + 97)
    for word in dictionary:
        if word in ans:
            print(ans)
            sys.exit()