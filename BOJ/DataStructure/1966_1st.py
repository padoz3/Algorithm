import sys
from collections import deque

input = sys.stdin.readline

N = int(input())

for _ in range(N):
    # 문서 개수 = n, 출력 순서가 궁금한 문서의 인덱스 m
    n, m = map(int, input().split())
    # 중요도 리스트 입력
    properties = list(map(int, input().split()))

    # (중요도, 원래 인덱스) 튜플 형태로 큐 생성
    queue = deque([p, idx] for idx, p in enumerate(properties))

    rank = 0

    while queue:
        # 현재 큐의 가장 앞에 있는 문서 꺼내기
        current = queue.popleft()

        # 현재 문서보다 더 중요한 문서가 하나라도 있는 경우
        if any(current[0] < other[0] for other in queue):
            queue.append(current)
        else:
            rank += 1
            if current[1] == m:
                print(rank)
                break
