import sys
import heapq
from collections import deque
sys.stdin = open('input.txt')

def bellman_ford(start):
    dists[start] = 0

    for i in range(N):
        for j in range(len(world)):
            node = world[j][0]
            next_node = world[j][1]
            dist = world[j][2]
            # 현재 간선을 거쳐서 다른 노드로 이동하는 거리가 더 짧은 경우
            if dists[next_node] > dists[node] + dist:
                dists[next_node] = dists[node] + dist

                # v번째 라운드에서도 값이 갱신된다면 음수 순환이 존재한다는 뜻
                if i == N - 1:
                    return False

    return True 

T = int(input())
INF = int(1e9)
for t in range(T):
    N, M, W = map(int, input().split())
    world = []
    dists = [INF] * (N + 1)

    # 도로의 정보 (양방향)
    for _ in range(M):
        S, E, T = map(int, input().split())
        world.append((S, E, T))
        world.append((E, S, T))

    # 웜홀의 정보 (단방향)
    for _ in range(W):
        S, E, T = map(int, input().split())
        world.append((S, E, -T))
    
    result = bellman_ford(1)

    if result:
        print(dists)
        print("NO")
    else:
        print('YES')


# def dijkstra(start_node):
#     # 누적 거리, 노드 번호
#     # hq = [(start_node, 0)]
#     hq = deque()
#     hq.append((start_node, 0))
#     # 거리를 저장하는 리스트
#     dists = [10000] * (N + 1)
#     # 시작 지점 초기화
#     dists[start_node] = 0
#     while hq:
#         print(hq)
#         # 노드, 거리
#         # node, dist = heapq.heappop(hq)
#         node, dist = hq.popleft()
#         # 이미 더 작게 방문한 적 있으면 continue
#         if dists[node] < dist:
#             continue
#
#         for next_node, next_dist in world[node]:
#             new_dist = dist + next_dist
#
#             # 다음 노드까지 가는 거리에 이미 작게 방문한 적이 있으면 continue
#             if dists[next_node] < new_dist:
#                 continue
#
#             # 처음으로 돌아왔을 경우 (다음에 방문할 노드가 시작 노드랑 같을 때)
#             # 같은 곳에서 같은 곳으로 이동할 경우
#             if next_node == start_node:
#                 if dist < 0:
#                     print(node, next_node)
#                     return dists[next_node]
#                 else:
#                     continue
#
#             # heapq.heappush(hq, (next_node, new_dist))
#             hq.append((next_node, new_dist))
#     return 0

# T = int(input())
# for t in range(T):
#     # 지점의 수, 도로의 개수, 웜홀의 개수
#     N, M, W = map(int, input().split())
#     world = [[] for _ in range(N+1)]
#
#     # 도로의 정보 (양방향)
#     for _ in range(M):
#         S, E, T = map(int, input().split())
#         world[E].append((S, T))
#
#     flag = 1
#     # 웜홀의 정보 (단방향)
#     for _ in range(W):
#         S, E, T = map(int, input().split())
#         world[S].append((E, -T))
#
#         if S == E:
#             flag = -T
#
#     for w in world:
#         print(*w)
#
#     # 어디서 출발할 지 모르기 때문에 모든 곳에서 출발시켜본다
#     if flag == 1:
#         for n in range(N+1):
#             if len(world[n]) == 0:
#                 continue
#             result = dijkstra(n)
#             print(result, n)
#             # 음수가 나오면 즉시 종료
#             if result < 0:
#                 break
#     else:
#         result = -1
#
#     # 0일 경우 실패임 그냥
#     if result >= 0:
#         print('NO')
#     else:
#         print('YES')




