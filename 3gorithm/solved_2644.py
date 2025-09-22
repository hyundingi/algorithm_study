from collections import deque

def bfs(start):
    global result
    queue = deque()
    queue.append(start)

    while queue:
        people = queue.popleft()

        if chonsu[people]:
            if p1 or p2 in chonsu[people]:
                result += 1
                
            for i in range(len(chonsu[people])):
                if visited[chonsu[people][i]]:
                    continue
                visited[chonsu[people][i]] = 1
                queue.append(chonsu[people][i])


n = int(input())
p1, p2 = map(int, input().split())
m = int(input())

chonsu = [[]] + [[] for _ in range(n)]
print(chonsu)
visited = [0] * (n + 1)
for i in range(m):
    a, b = map(int, input().split())
    chonsu[a].append(b)

print(chonsu)
result = 0
bfs(1)
print(result)