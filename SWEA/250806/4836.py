# test case
T = int(input())

# x,x ~ x,x, 까지 x 색깔

for t in range(T):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]

    # 격자
    area = [[0] * 10 for _ in range(10)]

    # 좌표 구하기
    for ping in arr:
        draw1 = ping[0:2]
        draw2 = ping[2:4]
        color = ping[-1]

        # 좌표 1 ~ 좌표 2까지 색칠 (area에 컬러 숫자를 더함)
        for i in range(draw1[0], draw2[0]+1):
            for j in range(draw1[1], draw2[1] + 1):
                area[i][j] += color

    # 보라색으로 변한 거 찾기
    count = 0
    for a in area:
        for b in a:
            if b == 3:
                count += 1

    print(f'#{t+1} {count}')
