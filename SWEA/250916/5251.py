import sys
from heapq import heappush, heappop

sys.stdin = open('input2.txt')

def dijkstra(start):
    # 누적거리 , 노드번호
    pq = [(0, start)]
    # 각 정점까지의 최단거리를 저장할 리스트
    inf = int(21e8)
    dists = [inf] * (N+1)
    dists[start] = 0  # 시작점 초기화

    while pq:
        dist, node = heappop(pq)
        # 이미 더 작은 값으로 온 적이 있으면 버린다
        if dists[node] < dist:
            continue

        for i in range(N+1):
            # 다음 노드로 가기 위한 누적 거리 계산
            # 누적 거리 = 현재까지의 거리 + 다음 거리
            if graph[node][i] == 0:
                continue

            new_dist = dist + graph[node][i]

            # 이미 작거나 같은 가중치로 온 적이 있다면 pass
            if new_dist >= dists[i]:
                continue

            # 누적 거리, 새로운 노드를 pq에 저장 + dists에 갱신
            dists[i] = new_dist
            heappush(pq, (new_dist, i))

    return dists
    # # 모든 정점을 다 돌아볼 때까지
    # dists[start] = 0
    # while True:
    #     min_node = INF
    #     if start == N:
    #         break
    #     path.append(start)
    #     # 모든 정점을 돌아보면서 거리 저장
    #     for i in range(N+1):
    #         dists[i] = min(dists[i], dists[start]+graph[start][i])
    #
    #     for i in range(start+1, N+1):
    #         if dists[i] == 0:
    #             continue
    #         if min_node > dists[i]:
    #             min_node, min_idx = dists[i], i
    #
    #     start = min_node
    #     print(start, dists)
    # return dists


T = int(input())
for t in range(T):
    N, E = map(int, input().split())

    # 인접행렬
    graph = [[0] * (N+1) for _ in range(N+1)]

    # 다익스트라는 단방향
    for _ in range(E):
        start, end, length = map(int, input().split())
        graph[start][end] = length

    # 0번 지점 부터 시작
    result = dijkstra(0)

    print(f'{t+1} {result[-1]}')



# 강사님 ------------------
T = int(input())
for t in range(T):
    nodes, edges = map(int, input().split())
    adj_list = [
        [] for _ in range(nodes + 1)
    ]

    INF = float('inf')
    # 간선 정보 입력
    for _ in range(edges):
        start, end, weight = map(int, input().split())
        adj_list[start].append((end, weight))

    # 현재 도달가능한 최단 거리 정보
    dists = [INF for _ in range(nodes + 1)]
    # 방문 표시용
    visited = [False for _ in range(nodes + 1)]
    # 시작점은 가는데 드는 비용이 0이다.
    dists[0] = 0

    # 정점의 갯수만큼 반복하면 된다.
    for _ in range(nodes + 1):

        # 1. 현재 도달 가능한 가장 가까운 정점을 찾는다.
        now = -1
        min_dist = INF
        for node in range(nodes + 1):
            if visited[node]:
                continue

            # 현재 살펴보고 있는 점이 더 가까우면
            if dists[node] < min_dist:
                now = node
                min_dist = dists[node]

        # 2. 해당 정점에 방문한다
        visited[now] = True

        # 3. 정점에 방문함으로서 도달 가능한 점들의 정보를 갱신한다.
        for node, weight in adj_list[now]:
            if visited[node]:
                continue

            # 내가 알고 있던 node 까지의 최저 비용
            # vs 여기까지 오는데 걸린 비용 + 여기에서 노드까지 가는데 드는 비용
            dists[node] = min(dists[node], dists[now] + weight)

    print(f'#{t + 1} {dists[nodes]}')
