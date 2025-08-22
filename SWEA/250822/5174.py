test_case = int(input())

for t in range(test_case):
    # 간선 수, root
    N, M = map(int, input().split())

    arr = list(map(int, input().split()))

    # N + 2 (노드 = 간선 +1, 인덱스 번호에 맞춰 받기 위해 +1)
    tree = [[0] * (N + 2) for _ in range(N + 1)]

    # 트리 만들기
    for i in range(len(arr)):
        # 부모값
        if i % 2 == 0:
            # 부모값의 인덱스
            node_p = arr[i]
        else:
            # 자식 값
            for j in range(len(tree[0])):
                if tree[j][node_p] == 0:
                    tree[j][node_p] = arr[i]
                    break

    # 기본값 설정
    nodes = []
    visit = [M, ]
    now = M
    end = 0

    # DFS
    while True:
        for i in range(N):
            if tree[i][now] != 0:
                nodes.append(tree[i][now])
                visit.append(tree[i][now])
            else:
                if len(nodes) == 0:
                    end = 1

        if end == 1:
            break

        now = nodes.pop()

    print(f'#{t+1} {len(visit)}')
