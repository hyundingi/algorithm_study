import sys
sys.stdin = open('input.txt')

from collections import deque

def bfs():
    q = deque()
    visited = [0] * (N+1)
    team = 0
    q.append(1)

    while q:
        now = q.popleft()
        visited[now] = 1

        for node in graph[now]:
            if visited[node]:
                team += 1
                continue
            
            q.append(node)



    return team




T = int(input())
for t in range(T):
    N, M = map(int, input().split())
    arr = list(map(int, input().split()))
    graph = [[] for _ in range(N+1)]

    for i in range(0, len(arr), M):
        a, b = arr[i], arr[i+1]
        # 양방향 인접 리스트 저장
        graph[a].append(b)
        graph[b].append(a)

    result = bfs()
    print(result)



