test_case = int(input())

for t in range(test_case):

    N, M = map(int, input().split())

    arr = [list(map(int, input().split())) for i in range(N)]

    # 최고합계
    sum_max = 0

    # 계산 가능한 범위 : 줄 길이 - (파리채크기 -1)
    # 파리채 크기 -1을 하는 이유는 패리채의 가장 왼쪽 줄은 포함해야하기 때문임
    for i in range(N-(M-1)):
        for j in range(N-(M-1)):

            # 죽은 파리 합계
            die_fly_sum = 0
            # 파리채 세로
            for m in range(M):
                # 파리채 가로
                for mm in range(M):
                    die_fly_sum += arr[i+m][j+mm]

            if die_fly_sum > sum_max:
                sum_max = die_fly_sum

    print(f'#{t+1} {sum_max}')