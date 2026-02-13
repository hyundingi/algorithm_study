import sys
from collections import deque
sys.stdin = open('input.txt')


def bfs(start):
    q = deque([start])
    visited = [False] * (N + 1)
    visited[start] = True
    count = 1

    while q:
        node = q.popleft()

        for n in network[node]:
            if visited[n]:
                continue
            q.append(n)
            visited[n] = True
            count += 1

    return count


N, M = map(int, input().split())
network = [[] for _ in range(N + 1)]

for _ in range(M):
    a, b = map(int, input().split())
    network[b].append(a)

results = []
max_hacked = -1

for i in range(1, N + 1):
    hacked = bfs(i)

    if hacked > max_hacked:
        max_hacked = hacked
        results = [i]

    elif max_hacked == hacked:
        results.append(i)

print(*(sorted(results)))


