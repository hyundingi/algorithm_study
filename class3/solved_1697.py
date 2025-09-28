from collections import deque

def bfs(N):
    global result

    queue = deque()
    queue.append(N)

    while queue:
        subin = queue.popleft()

        if subin == K:
            return 0
        
        for s in (subin-1, subin+1, subin*2):
            if s == K:
                return path[subin] + 1
            
            if 0 <= s <= 100000 and not path[s]:
                # 계산된 값 queue에 저장
                queue.append(s)
                # 계산된 값은 원래 값의 + 1 번째에 나올 수 있는 수임을 표시
                path[s] = path[subin] + 1


N, K = map(int, input().split())
path = [0] * 100001
result = bfs(N)
print(result)