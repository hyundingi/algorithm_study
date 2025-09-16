def make_set(n):
    parents = [i for i in range(n + 1)]
    return parents


# 대표 찾는 함수
def find_set(node):
    if parents[node] != node:
        return find_set(parents[node])
    return node


def union(x, y):
    # 각 원소 대표 찾기
    parent_x = find_set(x)
    parent_y = find_set(y)

    if parent_x < parent_y:
        parents[parent_y] = parent_x
    else:
        parents[parent_x] = parent_y


T = int(input())
for t in range(T):
    N, M = map(int, input().split())
    # 각자가 홀로 있는 서로소 집합을 만든다
    parents = make_set(N)

    # 간선 정보 받기
    all_edges = list(map(int, input().split()))

    # 간선 합집합 만들기
    for i in range(M):
        union(all_edges[i * 2], all_edges[i * 2 + 1])

    roots = set()
    for i in range(1, N + 1):
        roots.add(find_set(i))

    print(f'#{t+1} {len(roots)}')





# import sys
# sys.stdin = open('input.txt')

# from collections import deque

# def bfs():
#     q = deque()
#     visited = [0] * (N+1)
#     team = 0
#     q.append(1)

#     while q:
#         now = q.popleft()
#         visited[now] = 1

#         for node in graph[now]:
#             if visited[node]:
#                 team += 1
#                 continue
            
#             q.append(node)



#     return team




# T = int(input())
# for t in range(T):
#     N, M = map(int, input().split())
#     arr = list(map(int, input().split()))
#     graph = [[] for _ in range(N+1)]

#     for i in range(0, len(arr), M):
#         a, b = arr[i], arr[i+1]
#         # 양방향 인접 리스트 저장
#         graph[a].append(b)
#         graph[b].append(a)

#     result = bfs()
#     print(result)



