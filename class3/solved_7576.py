from collections import deque
import sys
sys.stdin = open('input.txt')

def all_visited():
    global days
    for i in range(N):
        for j in range(M):
            if visited[i][j] == 0:
                return -1
            
            days = max(days, visited[i][j])
    return days - 1

def bfs(queue):

    while queue:
        ny, nx = queue.popleft()

        if visited[ny][nx] == 0:
            visited[ny][nx] = 1

        for d in range(4):
            dy = ny + dys[d]
            dx = nx + dxs[d]

            if 0 <= dy < N and 0 <= dx < M:
                if tomatos[dy][dx] == 0 and visited[dy][dx] == 0:
                    queue.append((dy, dx))
                    visited[dy][dx] = visited[ny][nx] + 1

        for v in visited:
            print(*v)
        print('-'*10)
    # return


# m - 상자의 가로 , n - 세로
M, N = map(int, input().split())
tomatos = [list(map(int, input().split())) for _ in range(N)]
visited = [[0] * M for _ in range(N)]
days = cnt = 0
queue = deque()



# 1 : 익토 / 0 : 덜익토 / -1 : 없음
dys = [-1, 0, 1, 0]
dxs = [0, 1, 0, -1]

for i in range(N):
    for j in range(M):
        if tomatos[i][j] == 1:
            queue.append((i, j))
        elif tomatos[i][j] == -1:
             visited[i][j] = -1

bfs(queue)
print(all_visited())
