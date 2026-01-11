import sys
import math

input = sys.stdin.readline

N = int(input()) # 참가자 수
T_shirt = list(map(int, input().split()))
# 티셔츠 사이즈별 신청자 수
# S, M, L, XL, XXL, XXXL
T, P = map(int,input().split()) # 티셔츠 묶음 수, 펜 묶음 수

T_shirt_order = 0

for i in T_shirt:
    T_shirt_order += math.ceil(i / T)

P_order_set = N // P
p_order = N % P

print(T_shirt_order)
print(P_order_set, p_order)