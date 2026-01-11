import sys
import math

input = sys.stdin.readline

A, B, V = map(int, input().split())

day_count = 1

snail_height = 0
snail_daily_height = A - B
V -= A

day_count += math.ceil(V / snail_daily_height)

print(day_count)