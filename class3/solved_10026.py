import sys
from collections import deque
sys.stdin = open('input.txt')

def bfs(y, x):
    global cnt
    q = deque()
    q.append((y, x))
    visited[y][x] = cnt
    while q:
        y, x = q.popleft()

        for d in range(4):
            dy = y + dys[d]
            dx = x + dxs[d]

            if 0 <= dy < N and 0 <= dx < N and visited[dy][dx] == 0:
                if colors[y][x] == colors[dy][dx]:
                    visited[dy][dx] = cnt
                    q.append((dy, dx))

        # for v in visited:
        #     print(*v)
        # print('-' * 15)

def bfs2(y, x):
    global cnt2
    q = deque()
    q.append((y, x))
    visited2[y][x] = cnt2
    while q:
        y, x = q.popleft()

        for d in range(4):
            dy = y + dys[d]
            dx = x + dxs[d]

            if 0 <= dy < N and 0 <= dx < N and visited2[dy][dx] == 0:
                if colors[y][x] == 'B' and colors[dy][dx] == 'B':
                    visited2[dy][dx] = cnt2
                    q.append((dy, dx))

                if colors[y][x] in ['R', 'G'] and colors[dy][dx] in ['R', 'G']:
                    visited2[dy][dx] = cnt2
                    q.append((dy, dx))

        # for v in visited2:
        #     print(*v)
        # print('-' * 15)

N = int(input())
colors = [list(input()) for _ in range(N)]

# 서 북 동 남
dys = [0, -1, 0, 1]
dxs = [-1, 0, 1, 0]

visited = [[0] * N for _ in range(N)]
visited2 = [[0] * N for _ in range(N)]
cnt = 0
for y in range(N):
    for x in range(N):
        if visited[y][x] == 0:
            cnt += 1
            bfs(y, x)

cnt2 = 0
for y in range(N):
    for x in range(N):
        if visited2[y][x] == 0:
            cnt2 += 1
            bfs2(y, x)

print(cnt, cnt2)


# import sys
# from collections import deque
# sys.stdin = open('input.txt')


# def bfs(cnt):
#     global chk
#     q = deque()
#     start_y, start_x = find_start()
#     q.append((start_y, start_x))
#     visited[start_y][start_x] = cnt
#     while q:
#         y, x = q.popleft()

#         chk += 1

#         for d in range(4):
#             dy = y + dys[d]
#             dx = x + dxs[d]

#             if 0 <= dy < N and 0 <= dx < N and visited[dy][dx] == 0:
#                 if colors[y][x] == colors[dy][dx]:
#                     visited[dy][dx] = cnt
#                     q.append((dy, dx))

#         for v in visited:
#             print(*v)
#         print('-' * 15)

# def find_start():
#     for i in range(N):
#         for j in range(N):
#             if visited[i][j] == 0:
#                 return i, j

# def find_area():
#     for i in range(N):
#         for j in range(N):
#             if


# N = int(input())
# colors = [list(input()) for _ in range(N)]

# # 북 동 남 서
# dys = [-1, 0, 1, 0]
# dxs = [0, 1, 0, -1]

# visited = [[0] * N for _ in range(N)]
# visited_2 = [[0] * N for _ in range(N)]

# area = 1
# chk = 0
# s = set()

# while chk != N * N:
#     bfs(area)
#     area += 1

# result = find_area()
# print(area-1, result)
