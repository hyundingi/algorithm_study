import sys
from collections import deque

def dfs():
    global min_cnt
    q = deque()
    q.append((X, 0))

    while q:
        num, cnt = q.popleft()

        # num 이 1이 되었을 때 최소 횟수 저장
        if num == 1:
            min_cnt = min(cnt, min_cnt)

        # num이 0일 때 처리
        if num == 0:
            continue
        
        # 가지치기 - 이미 카운트가 최소 카운트보다 크면 끝
        if cnt > min_cnt:
            continue

        # num 이 3으로 나눠지는 수이면 나눔
        if num % 3 == 0:
            q.append((num // 3, cnt + 1))
        
        # num이 2로 나눠지는 수이면 나눔
        if num % 2 == 0:
            q.append((num // 2, cnt + 1))
        
        # 1을 뺀다
        q.append((num - 1, cnt + 1))
        

X = int(sys.stdin.readline())

min_cnt = X
dfs()
print(min_cnt)
