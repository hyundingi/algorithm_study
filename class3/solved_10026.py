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
