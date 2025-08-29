for t in range(10):
    n = int(input())
    # 트리 만들기
    tree = [[0]] + [input().split()[:2] for _ in range(n)]
    result = []
    count = 0

    # 후위 순회 사용
    def post_order(node, tree):
        global count
        if node < len(tree):
            post_order(node * 2, tree)  # 왼쪽 탐색
            post_order(node * 2 + 1, tree) # 오른쪽 탐색

            # 마지막 탐색에서 숫자일 경우 reslt 에 추가하고
            # 연산일 경우 리스트에서 값을 전부 꺼내 계산 후 다시 넣음
            if tree[node][1].isdigit():
                result.append(int(tree[node][1])) # 나 방문
                count += 1
            else:
                count += 1
                b = result.pop()
                a = result.pop()
                if tree[node][1] == '+':
                    result.append(a+b)
                elif tree[node][1] == '-':
                    result.append(a-b)
                elif tree[node][1] == '*':
                    result.append(a*b)
                elif tree[node][1] == '/':
                    result.append(a/b)
        print(result, count)
        if count == n:
            return result

    print(post_order(1, tree))
    # print(f'#{t+1} {result[0]:.0f}')

