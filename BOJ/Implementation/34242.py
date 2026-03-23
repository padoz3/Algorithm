S = input()
len_S = len(S)
total_score = 0

def get_score(idx):
    if idx < 0 or idx + 2 >= len_S:
        return 0
    sub = S[idx:idx+3]
    if sub == "+^+": return 1
    if sub == "-^-": return -1
    return 0

for i in range(len_S - 2):
    if S[i:i+3] == "+^+": total_score += 1
    if S[i:i+3] == "-^-": total_score -= 1
ans = total_score

for i in range(len_S):
    diff = 0

    # i 지우는 경우, i-2, i-1, i 패턴 사라짐
    diff -= get_score(i-2)
    diff -= get_score(i-1)
    diff -= get_score(i)

    # i 지워서 새로 생기는 패턴들
    if i - 2 >= 0 and i + 1 < len_S:
        new_sub1 = S[i-2] + S[i-1] + S[i+1]
        if new_sub1 == "+^+": diff += 1
        if new_sub1 == "-^-": diff -= 1
    if i - 1 >= 0 and i + 2 < len_S:
        new_sub2 = S[i-1] + S[i+1] + S[i+2]
        if new_sub2 == "+^+": diff += 1
        if new_sub2 == "-^-": diff -= 1
    ans = max(ans, total_score + diff)

print(ans)