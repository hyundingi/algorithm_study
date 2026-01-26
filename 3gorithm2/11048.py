import sys
from collections import deque

sys.stdin = open('input.txt')

dys = [0, 1, 1]
dxs = [1, 0, 1]

def is_range(y, x):
    if 0 < y <= N and 0 < x <= M:
        return True
    return False

def bfs(y, x):
    global result
    q = deque()
    q.append((y, x))
    visited[y][x] = grid[y][x]

    while q:
        y, x = q.popleft()
        for d in range(3):
            dy = y + dys[d]
            dx = x + dxs[d]

            if is_range(dy, dx):
                visited[dy][dx] = max(grid[dy][dx] + visited[y][x], visited[dy][dx])
                q.append((dy, dx))


N, M = map(int, input().split())
grid  = [[0] * (M+1)] + [[0] + list(map(int, input().split())) for _ in range(N)]
visited = [[0] * (M+1) for _ in range(N+1)]

bfs(1, 1)
print(visited[N][M])
