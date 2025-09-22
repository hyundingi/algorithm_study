# 상 하 좌 우
dys = [-1, 1, 0, 0]
dxs = [0, 0, -1, 1]

def recur():

    for y in range(n):
        for x in range(n):
            if visited[y][x]:
                continue

            for d in range(4):
                if 0 <= y + dys[d] < n and 0 <= x + dxs[d] < n: 
                    path.append(forest[y+dys[d]][x+dxs[d]])
                    recur()
                    path.pop()




n = int(input())
forest = [list(map(int, input().split())) for _ in range(n)]
visited = [[0] * n for _ in range(n)]
path = []
recur()

