"""
배추에 지렁이가 있으면 인접한 곳으로 이동할 수 있음
"""
import sys
sys.stdin = open('input.txt')

# 남 동 북 서
dys = [1, 0, -1, 0]
dxs = [0, 1, 0, -1]

# 인접한 배추에 방문체크 하는 함수
def check(y, x):
    cnt = 0
    while cnt < 4:
        for i in range(4):
            # 인덱스 범위를 벗어나지 않고,
            if -1 < y+dys[i] < M and -1 < x + dxs[i] < N:

                # 방문한 적 없고,
                if visited[y+dys[i]][x+dxs[i]] == 1:
                    cnt += 1
                    continue

                # 배추가 심어져있으면 방문 처리, y, x 재할당 후 break
                if farm[y+dys[i]][x+dxs[i]] == 1:
                    visited[y+dys[i]][x+dxs[i]] = 1
                    y, x = y+dys[i], x+dxs[i]
                    print(y, x)
                    break

                # 배추가 안 심겨있을 때
                else:
                    cnt += 1

    return 1



T = int(input())
for t in range(T):
    # 가로길이, 세로길이, 배추 개수
    M, N, K = map(int, input().split())
    farm = [[0] * M for _ in range(N)]
    visited = [[0] * M for _ in range(N)]
    result = 0

    # 배추 위치 받기
    for _ in range(K):
        x, y = map(int, input().split())
        farm[y][x] = 1

    for f in farm:
        print(f)
    print('--------밭')

    # 인접한 위치에 배추가 있으면 방문표시 반복
    for i in range(N):
        for j in range(M):
            if visited[i][j] == 1:
                continue
            if farm[i][j] == 1:
                visited[i][j] = 1
                result += check(i, j)

                print('방문-----------')
                for v in visited:
                    print(v)

    print(result)

