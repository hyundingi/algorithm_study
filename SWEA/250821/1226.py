for t in range(10):
    test_case = int(input())
    maze = [list(map(int, input().strip())) for _ in range(16)]

    delta = [[1, 0], [0, 1], [-1, 0], [0, -1]]
    # 출발점 , 도착점
    for i in range(16):
        for j in range(16):
            if maze[i][j] == 2:
                start_x, start_y = i, j
            elif maze[i][j] == 3:
                goal_x, goal_y = i, j

    # 현재 위치
    now_x, now_y = start_x, start_y

    # 돌아올 곳
    stack = []

    # 방문했는지
    visited = [[0] * 16 for _ in range(16)]

    # 출발지 방문 인증
    visited[start_x][start_y] = 1

    while True:

        # 델타 돌려서 갈 수 있는 곳 모두 스택함
        for dx, dy in delta:
            if maze[now_x+dx][now_y+dy] != 1 and visited[now_x+dx][now_y+dy] == 0:
                stack.append([now_x+dx, now_y+dy])

        # 미로 탈출 실패
        if len(stack) == 0:
            result = 0
            break

        # 갈 수 있는 곳 pop > 이동 > 방문 인증
        now = stack.pop()
        now_x, now_y = now[0], now[1]
        visited[now_x][now_y] = 1

        # 3을 만나면 종료
        if maze[now_x][now_y] == 3:
            result = 1
            break

    print(f'#{test_case} {result}')

