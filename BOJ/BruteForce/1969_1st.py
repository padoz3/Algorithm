import sys

input = sys.stdin.readline

N, M = map(int, input().split())
dna_list = [input().strip() for _ in range(N)]

ans = []
hd_sum = 0
nu_list = ['A', 'C', 'G', 'T']

# zip(*dna_list)를 하면 세로줄끼리 묶임
for col in zip(*dna_list):
    # A, C, G, T 순서대로 각 문자 개수 세기
    cnt_list = [col.count('A'), col.count('C'), col.count('G'), col.count('T')]

    # 가장 많이 나온 인덱스 찾기
    max_idx = max(cnt_list)
    # 그에 해당하는 뉴클레오타이드의 인덱스 찾기 -> 알파벳 인덱스 찾기
    idx = cnt_list.index(max_idx)

    # 결과 저장
    ans.append(nu_list[idx])

    # 틀린 개수 더하기
    hd_sum += (N - max_idx)

print(''.join(ans))
print(hd_sum)