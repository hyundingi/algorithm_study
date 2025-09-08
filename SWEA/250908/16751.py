T = int(input())
for t in range(T):
    N = int(input())
    schedules = [list(map(int, input().split())) for _ in range(N)]

    # 종료 시간을 기준으로 종료된다
    schedules.sort(key=lambda x:x[1])
    cnt = 1
    i = j = 0

    while i < N-1:
        # 끝나는 시간이 다음에 나오는 작업 시간의 시작시간보다 작은 경우
        if schedules[i][1] <= schedules[i+j][0]:
            # 카운트 + 1
            cnt += 1
            # i 값 셋팅
            i += j
            # j값 초기화
            j = 0

        # j를 하나씩 늘려가면서 끝시간이 시작시간보다 작은 경우를 찾음
        j += 1

        if i + j > N-1:
            break


    print(f'#{t+1} {cnt}')


