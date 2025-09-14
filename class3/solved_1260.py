"""
dfs 와 bfs
"""
from collections import deque

def dfs(start):
    q = deque()
    q.append(start)
    visited = [0] * (N + 1)
    
    while q:
        now = q.popleft()
        print(now)
        visited[now] = 1







N, M, V = map(int, input().split())
matrix = [[0] for _ in range(N+1)]

for _ in range(M):
    a, b = map(int, input().split())
    matrix[a].append(b)

dfs(V)


