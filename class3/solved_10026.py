import sys
sys.stdin = open('input.txt')


def bfs():
    area = 1
    for y in range(1, N):
        for x in range(N):
            next_x = x + 1

            if 0 <= next_x < N: 
                if colors[y][x] == colors[y][x+1] or colors[y][x] == colors[y-1][x]:
                    visited[y][x] = area
                
                else:
                    area += 1
                    visited[y][x] = area

            
        for v in visited:
            print(*v)
        print('-'*15)
                


N = int(input())
colors = [list(input()) for _ in range(N)]

# 북 동 남 서
dys = [-1, 0, 1, 0]
dxs = [0, 1, 0, -1]

visited = [[0] * N for _ in range(N)]

bfs()


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
