from collections import deque

def bfs(start):
    result = 0
    queue = deque()
    queue.append((start, 0))

    while queue:
        people, cs = queue.popleft()
        # print(people, cs)
        if chonsu[people]: 
            if visited[people]:
                continue 

            if people == p2:
                return cs 

            for i in range(len(chonsu[people])):
                if visited[people]:
                    continue 
                queue.append((chonsu[people][i], cs + 1))
            
            visited[people] = 1


        # print(chonsu[people], result)
    return -1


n = int(input())
p1, p2 = map(int, input().split())
m = int(input())

chonsu = [[]] + [[] for _ in range(n)]
visited = [0] * (n + 1)

for i in range(m):
    a, b = map(int, input().split())
    chonsu[a].append(b)
    chonsu[b].append(a)

# print(chonsu)
result = bfs(p1)
print(result)