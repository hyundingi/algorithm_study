import sys
from collections import deque

sys.stdin = open('input.txt')

def bfs(n):
    global result
    visited[n] = 1
    q = deque()
    q.append((n, 0))

    while q:
        val, cnt = q.popleft()

        if cnt > 2:
            continue

        result += 1

        for friend in friends[val]:
            if visited[friend] == 0:
                visited[friend] = 1
                q.append((friend, cnt+1))

n = int(input())
m = int(input())
friends = [[] for _ in range(n+1)]
visited = [0 for _ in range(n+1)]
result = 0

for _ in range(m):
    a, b = map(int, sys.stdin.readline().split())
    friends[a].append(b)
    friends[b].append(a)


bfs(1)
print(result-1)

