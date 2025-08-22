for t in range(10):
    N = int(input())

    arr = [input().split() for _ in range(N)]
    result = []

    # 중위순회 함수
    def inorder(node, tree):
        if node < len(tree):
            inorder(node * 2, tree)  # 먼저 왼쪽을 간다.
            result.append(tree[node])  # 그 다음 나를 방문
            inorder(node * 2 + 1, tree)  # 마지막 오른쪽 방문
        if len(result) == len(tree) - 1:
            return result

    words = [0]
    # 문자 저장
    for i in range(N):
        for j in range(len(arr[i])):
            if j == 1:
                words.append(arr[i][j])


    tree = [0]
    # tree 만들기
    for i in range(N):
        tree.append(arr[i][0])

    # 출력

    result_list = inorder(1, tree)

    print(f'#{t+1}', end=' ')
    for r in result_list:
        i = int(r)
        print(words[i], end='')
    print()




