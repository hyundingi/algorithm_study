
def recur(row, s):
    global result
    if row == N:
        # 가장 작은 합 찾기
        result = min(result, sum(path))
        return

    # 가지치기 - 최솟값보다 이미 크면 가망없음
    if s > result:
        return

    for i in range(N):
        if visited[i] == 1:
            continue
        path.append(factory[row][i])
        visited[i] = 1
        recur(row + 1, sum(path))
        path.pop()
        visited[i] = 0


T = int(input())
for t in range(T):
    N = int(input())
    factory = [list(map(int, input().split())) for _ in range(N)]

    # 저장용
    path = []
    # 방문 기록용
    visited = [0] * N
    # 가장 낮은 값을 구하기 위해 초기값을 최댓값으로 설정
    result = 99 * N

    recur(0, result)

    print(f'#{t+1} {result}')
