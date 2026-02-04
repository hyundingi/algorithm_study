import sys
from collections import deque
sys.stdin = open('input.txt')


def hack(n):
    q = deque()
    q.append(n)
    visited[n] = True

    while q:
        node = q.popleft()

        for i in range(len(network[node])):
            q.append(network[node][i])
            visited[network[node][i]] = True


N, M = map(int, input().split())
network = [[0] for _ in range(N + 1)]
visited = [False] * (N + 1)
cnt = [0] * (N + 1)

for _ in range(M):
    a, b = map(int, input().split())
    network[b].append(a)

for i in range(1, N + 1):
    hack(i)

