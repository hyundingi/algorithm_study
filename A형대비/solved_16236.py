import sys
from collections import deque
sys.stdin = open('input.txt')

"""
이동 - 아기 상어 보다 작거나 같은 칸
먹기 - 아기 상어 보다 작은 값
    - 거리가 가장 가까운데 있는 물고기를 먹으러 간다
        - 가장 위에, 가장 왼쪽이 우선
    - 자신의 크기와 같은 수의 물고기를 먹으면 크기 + 1
"""

dys = [0, 1, 0, -1]
dxs = [1, 0, -1, 0]

def bfs(y, x):
    q = deque()
    q.append((y, x))

    visited = [[-1] * N for _ in range(N)]
    visited[y][x] = 0

    fishes = []

    while q:
        y, x = q.popleft()

        for d in range(4):
            dy = y + dys[d]
            dx = x + dxs[d]

            if 0 <= dy < N and 0 <= dx < N:
                if grid[dy][dx] > shark:
                    continue
                if visited[dy][dx] != -1:
                    continue
                q.append((dy, dx))
                visited[dy][dx] = visited[y][x] + 1

                if 0 < grid[dy][dx] < shark:
                    fishes.append((visited[dy][dx], dy, dx))
    
    if not fishes:
        return None
    
    fishes.sort()
    return fishes[0]

N = int(input())
grid = [list(map(int, input().split())) for _ in range(N)]
fishes = []

# 아기 상어 위치 찾기
for i in range(N):
    for j in range(N):
        if grid[i][j] == 9:
            baby_y, baby_x = i, j
            grid[i][j] = 0


# 상어 크기, 먹은 물고기, 최종 출력
shark, eat, result = 2, 0, 0

while True:
    target = bfs(baby_y, baby_x)
    if target is None:
        break

    sec, baby_y, baby_x = target    
    print(target)
    eat += 1
    result += sec

    # 물고기 먹으면 0으로 변경
    grid[baby_y][baby_x] = 0

    if eat == shark:
        shark += 1
        eat = 0

    # print(baby_y, baby_x, sec, shark)
print(result)





