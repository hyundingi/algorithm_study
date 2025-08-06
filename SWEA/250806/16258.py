# test case
T = int(input())

for t in range(T):
    N = int(input())

    arr = [list(map(int, input().split())) for _ in range(N)]

    # 델타값 설정
    di = [0, 1, 0, -1]
    dj = [1, 0, -1, 0]

    # 절대값의 합을 받는 변수
    abs_sum = 0
    for i in range(N):
        for j in range(N):

            # 가운데 숫자
            number = arr[i][j]
            for d in range(4):
                ni = i + di[d]
                nj = j + dj[d]

                # 계산된 인덱스번호가 범위 안에 있는지 확인
                if 0 <= ni < N and 0 <= nj < N:

                    # 절대값의 합 계속 누적
                    abs_sum += abs(arr[ni][nj] - number)

    print(f'#{t+1} {abs_sum}')

