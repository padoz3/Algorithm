import sys

input = sys.stdin.readline

input_list = []

for i in range(3):
    x = input().strip()
    input_list.append(x)

ans_num = 0

for i in range(3):
    if input_list[i].isdecimal() == True:
        ans_num = int(input_list[i]) + 3 - i
        break

if ans_num % 3 == 0:
    if ans_num % 5 == 0:
        print("FizzBuzz")
    else:
        print("Fizz")
elif ans_num % 5 == 0:
    print("Buzz")
else:
    print(ans_num)