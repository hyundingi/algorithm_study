# V개의 노드개수, E개의 간선 정보 (방향성 x)
V, E = map(int, input().split())
# 선들 입력 받기
edges = [list(map(int, input().split())) for _ in range(E)]

# 먼저 그래프를 데이터로 표현해야 한다.
# ----------- 그래프 표현 방법 -----------------------------
# 인접 행렬
# 2차원 배열을 만들고, arr[i][j]가 true 라면 i > j로 통하는 길이 있음을 나타내도록 값을 채움
# 1. 전체 배열을 만든다 / N * N
adj_matrix = [
    [0] * (V + 1) for _ in range(V + 1)
]
# 2. 각 간선을 살펴보면서 adj_matrix 를 채운다
for edge in edges:
    # edge[0], edge[1] 까지는 길이 존재함을 의미
    adj_matrix[edge[0]][edge[1]] = 1

    # 양방향이라면?
    # edge[1]에서 edge[0]까지 길도 존재한다
    # adj_matrix[edge[1]][edge[0]] = 1

for row in adj_matrix:
    print(row)

# 인접 리스트 ------------------------------------------------
# 2차원 배열을 만들고 arr[i]에 리스트 또는 다른 자료형을 할당한 다음
# i에 저장된 리스트에 연결된 정점들을 넣어준다.

# 1. 각 i와 연결된 점들 보관을 위한 리스트만 만든다.
adj_lst = [
    [] for _ in range(V + 1)
]

# 2. 각 간선을 살펴보면서 adj_list 를 갱신한다
for edge in edges:
    # edge[0]에서 edge[1]이 도달 가능함을 의미함으로
    adj_lst[edge[0]].append(edge[1])
    # 양방향
    # adj_lst[edge[1]].append(edge[0])

for row in adj_lst:
    print(row)


# DFS 구현 -------------------------------------------------------
# 1. 재방문 방지를 위한 방문 배열 생성
visited = [0 for _ in range(V + 1)]

# 2. 출발 지점과 끝 지점 기록
start, goal = map(int, input().split())
visited[start] = 1

# 3. 진행 경로를 저장할 리스트 생성 (선택)
route = []

# 4. stack으로 만든다
# 스택을 팝을 하며 움직이는데 , 처음에 갈 곳은 start 이다
stack = [start]

# stack이 비어있지 않는 동안 반복
while stack:
    # 1. 이전 방문 지점 가져옴
    now = stack.pop(0)
    # 2. 방문 순서 기록
    route.append(now)
    # 3. 다음 방문 가능 점들을 넣어준다.
    for next_node in adj_lst[now]:
        # 연결되어 있고, 방문한 적 없으면 stack에 넣어주고 방문 표시
        if visited[next_node] == 0:
            stack.append(next_node)
            visited[next_node] = 1

print('DFS')
print(route)
print(visited[goal])
print()

# BFS 구현 --------------------------------------------------------
for i in range(V + 1):
    visited[i] = False
visited[start] = 1

route = []

queue = [start]

# queue 가 비어있지 않은 동안 반복
while queue:
    # 1. 이번 방문 지점을 가져온다
    now = queue.pop(0)
    # 2. 방문 순서를 기록한다.
    route.append(now)
    # 3. 다음 방문 가능 점들을 넣어준다.
    for next_node in adj_lst[now]:
        # 연결되어 있고, 방문한 적 없으면 stack > 방문 표시
        if visited[next_node] == 0:
            queue.append(next_node)
            visited[next_node] = 1

print('BFS')
print(route)
print(visited[goal])
