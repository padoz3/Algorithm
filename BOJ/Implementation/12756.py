import sys

input = sys.stdin.readline

a_a, a_hp = map(int, input().split())
b_a, b_hp = map(int, input().split())

while a_hp > 0 and b_hp > 0:
    a_hp -= b_a
    b_hp -= a_a

if a_hp > 0 and b_hp <= 0:
    print("PLAYER A")
elif b_hp > 0 and a_hp <= 0:
    print("PLAYER B")
else:
    print("DRAW")