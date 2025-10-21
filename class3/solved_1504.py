import sys
from collections import deque
sys.stdin = open('input.txt')

"""
1번에서 N번으로 이동 
임의로 주어진 두 정점은 반드시 통과해야한다
한 번 이동 했던 간선, 정점 모두 이동 가능
최단 경로로 이동
"""

def bfs():
    total = 0
    q = deque()
    q.append((1, 0))

    while q:
        node, length = q.popleft()

        if node == N:
            if v1 and v2 in path:
                return total

        for i in range(len(nodes[node])):
            q.append(nodes[node][i])



# 정점개수 , 간선개수
N, E = map(int, input().split())
nodes = [0] * (N+1)
# nodes = [[0] * (N+1) for _ in range(N+1)]
# a, b, c == 정점1, 정점2, 거리
for e in range(E):
    a, b, c = map(int, input().split())

    # nodes에 저장
    nodes[a].append((b, c))
    nodes[b].append((a, c))

    # nodes[a][b] = c
    # nodes[b][a] = c

# 반드시 거쳐야 하는 두 개의 서로 다른 정점 번호
v1, v2 = map(int, input().split())

bfs()
