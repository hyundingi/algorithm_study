from collections import deque
import sys
sys.stdin = open('input.txt')

def bfs(y, x):
    global result
    queue = deque()
    queue.append((y, x))

    while queue:
        ny, nx = queue.popleft()
        if visited[ny][nx] == 1:
            continue

        for d in range(4):
            dy = ny + dys[d]
            dx = nx + dxs[d]

            if 0 <= dy < N and 0 <= dx < M:
                if tomatos[dy][dx] == 0 and visited[dy][dx] == 0:
                    visited[dy][dx] = 1
                    queue.append((dy, dx))

        result += 1
        for v in visited:
            print(*v)
        print('-'*10)
    return


# m - 상자의 가로 , n - 세로
M, N = map(int, input().split())
tomatos = [list(map(int, input().split())) for _ in range(N)]
visited = [[0] * M for _ in range(N)]

# 1 : 익토 / 0 : 덜익토 / -1 : 없음
dys = [-1, 0, 1, 0]
dxs = [0, 1, 0, -1]

result = 0
for i in range(N):
    for j in range(M):
        if tomatos[i][j] == 1:
            bfs(i, j)
print(result)