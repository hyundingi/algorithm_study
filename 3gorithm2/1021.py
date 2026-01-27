from collections import deque

N, M = map(int, input().split())
targets = list(map(int, input().split()))

# 덱 생성
q = deque(range(1, N+1))
cnt = 0

for target in targets:
    while True:
        if q[0] == target:
            q.popleft()
            break
        else:
            target_idx = q.index(target)
            # 절반 지점보다 앞쪽에 있으면 왼쪽으로 회전
            if target_idx <= len(q) // 2:
                q.rotate(-1)
                cnt += 1
            # 뒤쪽에 있으면 오른쪽으로 회전
            else:
                q.rotate(1)
                cnt += 1

print(cnt)
