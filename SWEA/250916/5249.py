import sys
sys.stdin = open('input2.txt')

T = int(input())
for t in range(T):
    nodes, edges = map(int, input().split())
    adj_list = [
        [] for _ in range(nodes + 1)
    ]

    INF = float('inf')
    # 간선 정보 입력
    for _ in range(edges):
        node1, node2, weight = map(int, input().split())
        adj_list[node1].append((node2, weight))
        adj_list[node2].append((node1, weight))

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
            # vs 트리에서 노드까지 가는데 드는 비용
            dists[node] = min(dists[node], weight)

    print(f'#{t + 1} {sum(dists)}')
