import sys
sys.stdin = open("input.txt")

from collections import deque

# 깊이 우선 탐색
def dfs(start):
    # 방문한 곳 체크
    visited[start] = 1
    print(start, end=' ')
    # 양방향으로 넣은 값을 정렬해준다 . (낮은 값 부터 먼저 !)
    for now in sorted(matrix[start]):
        # 방문한 적 있으면 pass
        if visited[now]:
            continue
        # 재귀호출
        dfs(now)

# 넓이 우선 탐색
def bfs(start):
    # 큐를 활용한다
    q = deque()
    q.append(start)
    while q:
        now = q.popleft()

        # 이미 방문한 적 있으면 pass
        if visited[now]:
            continue

        visited[now] = 1
        print(now, end=' ')
        
        # 갈 수 있는 애들을 q에 저장해놓고 가장 먼저 넣은 거 부터 차례차례 뺀다
        for node in sorted(matrix[now]):
            q.append(node)



N, M, V = map(int, input().split())
# 인접 리스트로 저장
matrix = [[] for _ in range(N + 1)]
for _ in range(M):
    a, b = map(int, input().split())
    matrix[a].append(b)
    matrix[b].append(a) # 양방향 데이터 저장

visited = [0] * (N + 1)
dfs(V)
visited = [0] * (N + 1)
print()
bfs(V)



