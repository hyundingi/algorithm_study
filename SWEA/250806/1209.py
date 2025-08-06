# test case

for _ in range(10):
    test_case = int(input())

    arr = [list(map(int, input().split())) for _ in range(100)]
    # 최댓값
    max_sum = 0

    for i in range(100):
        # 합을 받는 변수
        total = 0

        for j in range(100):              # 행의 합
            total += arr[i][j]
            if total > max_sum:
                max_sum = total

        # 합을 받는 변수
        total = 0

        for j in range(100):               # 열의 합
            total += arr[j][i]
            if total > max_sum:
                max_sum = total

        # 합을 받는 변수
        total = 0
        for j in range(99, -1, -1):         # 반대 대각선의 합
            total += arr[i][j]
            if total > max_sum:
                max_sum = total
        
        # 합을 받는 변수
        total = 0
        for j in range(100):               # 정 대각선의 합
            total += arr[j][j]
            if total > max_sum:
                max_sum = total

    print(f'#{test_case} {max_sum}')

