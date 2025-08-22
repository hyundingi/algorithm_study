def bfs(s, v):
    # 초기화
    visited = [0] * (V + 1)  # visited 생성
    queue = [s]  # 큐 생성, 시작점 인큐
    visited[s] = 1  # 시작점 방문 표시

    # 반복
    while queue:  # 탐색할 정점이 남아있으면
        t = queue.pop(0)   # 디큐
        print(t)          # visit(), 방문 접점 출력
        for w in adj_lst[t]:     # 인접하고 미방문인 정점 인큐, 인큐 표시
            if visited[w] == 0:
                queue.append(w)
                visited[w] = visited[t] + 1

    return


V, E = map(int, input().split())  # 마지막 정점, 간선 수
arr = list(map(int, input().split()))

# 인접 리스트
adj_lst = [[] for _ in range(V + 1)]  # v번행까지 준비

# 1
for i in range(E):
    v1, v2 = arr[i * 2], arr[i * 2 + 1]

    # 2
    # for i in range(0, E*2, 2):
    #	 v1, v2 = arr[i], arr[i+1]

    adj_lst[v1].append(v2)
    adj_lst[v2].append(v1)  # 방향표시가 없는 경우

bfs(1, 6)