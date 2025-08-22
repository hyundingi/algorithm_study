# V개의 노드개수, E개의 간선 정보 (방향성 x)
V, E = map(int, input().split())

# 그래프
arr = [input().split() for _ in range(E)]

# 시작점, 도착점
S, E = map(int, input().split())

# 방문 체크
visited = [0] * V

for i in range(V):
    if arr[i][0] == S:
print(arr)