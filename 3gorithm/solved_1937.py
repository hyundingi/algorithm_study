from collections import deque

# 상 하 좌 우
dys = [-1, 1, 0, 0]
dxs = [0, 0, -1, 1]

def bfs(y, x):
    visited = [[0] * n for _ in range(n)]
    queue = deque()
    queue.append((y,x))
    cnt = 0
    while queue:
        y, x = queue.popleft()
        visited[y][x] = 1

        for d in range(4):
            ny = y + dys[d]
            nx = x + dxs[d]

            # 인덱스 에러 방지
            if 0 <= ny < n and 0 <= nx < n:
                # 상 하 좌 우 에 나보다 큰 값이 있는지 확인
                if forest[y][x] < forest[ny][nx]:
                    # 방문한 적 있으면 pass
                    if visited[ny][nx]:
                        continue
                    queue.append((ny, nx))
                    cnt += 1

    return cnt



n = int(input())
forest = [list(map(int, input().split())) for _ in range(n)]

result = 0
for i in range(n):
    for j in range(n):
        a = bfs(i, j)
        result = max(a, result)

print(result)
