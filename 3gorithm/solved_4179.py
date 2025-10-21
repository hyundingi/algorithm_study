import sys
from collections import deque
sys.stdin = open('input.txt')

"""
1. 지훈이가 불에 타기전에 탈출할 수 있는지?
2. 얼마나 빨리 탈출할 수 있는지?
3. 지훈이와 불은 수평 혹은 수직으로 이동한다. 
4. 불은 네방향으로 확산된다 
5. 지훈이는 미로의 가장자리에 접한 공간에서 탈출
6. 지훈이와 불은 벽이 있는 공간은 통과하지 못함 
"""
# 우 하 좌 상
dys = [0, 1, 0, -1]
dxs = [1, 0, -1, 0]

def bfs(jy, jx, fire_q):
    q = deque()
    q.append((jy, jx, 0))
    visited[jy][jx] = 1

    while q:
        y, x, cnt = q.popleft()
        # print(q)
        for d in range(4):
            dy = y + dys[d]
            dx = x + dxs[d]

            if 0 <= dy < R and 0 <= dx < C:
                if miro[dy][dx] == '.' and visited[dy][dx] == 0:
                    if fire_time[dy][dx] == -1 or fire_time[dy][dx] > cnt + 1:
                        visited[dy][dx] = 1
                        q.append((dy, dx, cnt + 1))
            else:
                return cnt + 1

    return 'IMPOSSIBLE'

def wide_fire():
    while fire_q:
        y, x = fire_q.popleft()
        cnt = fire_time[y][x]
        for d in range(4):
            dy = y + dys[d]
            dx = x + dxs[d]

            if 0 <= dy < R and 0 <= dx < C:
                if miro[dy][dx] != '#' and fire_time[dy][dx] == -1:
                    fire_time[dy][dx] = cnt + 1
                    fire_q.append((dy, dx))


# def wide_fire(fire_q):
#     for i in range(len(fire_q)):
#         y, x = fire_q.popleft()
#
#         for d in range(4):
#             dy = y + dys[d]
#             dx = x + dxs[d]
#
#             if 0 <= dy < R and 0 <= dx < C and miro[dy][dx] == '.':
#                 miro[dy][dx] = 'F'
#                 fire_q.append((dy, dx))
#
#     return fire_q
#
# last_cnt = -1
# def chg_cnt(cnt):
#     global last_cnt
#
#     if last_cnt == cnt:
#         return False
#
#     last_cnt = cnt
#     return True

R, C = map(int, sys.stdin.readline().split())
miro = [list(sys.stdin.readline()) for _ in range(R)]
visited = [[0] * C for _ in range(R)]

# 불 계산
fire_q = deque()
fire_time = [[-1] * C for _ in range(R)]

for r in range(R):
    for c in range(C):
        if miro[r][c] == 'J':
            ji_y, ji_x = r, c

        if miro[r][c] == 'F':
            fire_q.append((r, c))
            fire_time[r][c] = 0

wide_fire()
for i in fire_time:
    print(*i)

print(bfs(ji_y, ji_x, fire_q))
