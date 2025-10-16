import sys
from collections import deque
sys.stdin = open('input.txt')

def bfs(now, cnt):
    q = deque()
    q.append((now, cnt))

    while q:
        floor, cnt = q.popleft()

        if floor == G:
            return cnt

        if floor <= 0 or floor > F:
            continue

        if visited[floor]:
            continue

        q.append((floor + U, cnt + 1))
        q.append((floor - D, cnt + 1))
        visited[floor] = 1

    return "use the stairs"




# 건물 총 높이, 현재 위치, 도착지, 올라가기, 내려가기
F, S, G, U, D = map(int, input().split())
result = 1e9
visited = [0] * (F + 1)
print(bfs(S, 0))
