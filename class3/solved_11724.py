N, M = map(int, input().split())

graph = [[] * N]


for m in range(M):
    start, end = map(int, input().split())
    graph[start].append(end)
    graph[end].append(start)


