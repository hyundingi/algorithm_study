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

def find_fish(y, x):
    global shark
    fish_y, fish_x = 100, 100
    idx = 0
    for i in range(len(fishes)):
        if fishes[i][0] == 0:
            continue
        if fishes[i][0] < shark:
            # 더 가까이에 있는 거 찾기
            if abs(y - fish_y) + abs(x - fish_x) > abs(y - fishes[i][1]) + abs(x - fishes[i][2]):
                fish_y = fishes[i][1]
                fish_x = fishes[i][2]
                idx = i
            # 거리가 같을 때
            elif abs(y - fish_y) + abs(x - fish_x) == abs(y - fishes[i][1]) + abs(x - fishes[i][2]):
                # 더 위에 있는 거 먼저 찾기
                if fish_y > fishes[i][1]:
                    fish_y = fishes[i][1]
                    fish_x = fishes[i][2]
                    idx = i
                # 높이도 같을 때
                elif fish_y == fishes[i][1]:
                    # 더 왼쪽에 있는 거 찾기
                    if fish_x > fishes[i][2]:
                        fish_y = fishes[i][1]
                        fish_x = fishes[i][2]
                        idx = i
    print(fishes)
    print(shark)
    fishes[idx][0] = 0
    return fish_y, fish_x



def bfs(y, x, sec):
    q = deque()
    q.append((y, x, sec))
    fish_y, fish_x = find_fish(y, x)
    if fish_y == 100:
        return 0, 0, 0
    visited = [[0] * N for _ in range(N)]
    while q:
        y, x, sec = q.popleft()
        if fish_y == y and fish_x == x:
            print(y, x, sec)
            return y, x, sec

        for d in range(4):
            dy = y + dys[d]
            dx = x + dxs[d]

            if 0 <= dy < N and 0 <= dx < N:
                if grid[dy][dx] > shark:
                    continue
                if visited[dy][dx]:
                    continue
                q.append((dy, dx, sec + 1))
                visited[dy][dx] = 1
    print(y,x,sec)
    return y, x, sec

N = int(input())
grid = [list(map(int, input().split())) for _ in range(N)]
fishes = []

# 아기 상어 위치 찾기
for i in range(N):
    for j in range(N):
        if grid[i][j] == 9:
            baby_y, baby_x = i, j

        elif grid[i][j] != 0:
            fishes.append([grid[i][j], i, j])

fishes = sorted(fishes, key=lambda x:x[0])
print(fishes)
# 상어 크기, 먹은 물고기
shark, eat, result = 2, 0, 0
for i in range(len(fishes)):
    baby_y, baby_x, sec = bfs(baby_y, baby_x, 0)
    if sec == 0:
        break
    eat += 1
    result += sec
    if eat == shark:
        shark += 1
        eat = 0

print(result)





