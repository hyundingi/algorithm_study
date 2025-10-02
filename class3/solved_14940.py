from collections import deque
import sys
sys.stdin = open('input.txt')

N, M = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(N)]
visited = [[0] * M for _ in range(N)]

dys = [0, 1, 0, -1]
dxs = [1, 0, -1, 0]

def bfs(y, x):
    q = deque()
    cnt = 0
    q.append((y, x))
    visited[y][x] = cnt
    while q:
        y, x = q.popleft()

        for d in range(4):
            dy = y + dys[d]
            dx = x + dxs[d]

            if 0 <= dy < N and 0 <= dx < M and grid[dy][dx] == 1 and visited[dy][dx] == 0:
                q.append((dy, dx))
                visited[dy][dx] = visited[y][x] + 1


def dont_move():
    for i in range(N):
        for j in range(M):
            if visited[i][j] == 0 and grid[i][j] == 1:
                visited[i][j] = -1




for i in range(N):
    for j in range(M):
        if grid[i][j] == 2:
            bfs(i, j)
            break

dont_move()

for n in range(N):
    print(*visited[n])