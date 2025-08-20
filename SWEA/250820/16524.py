test_case = int(input())

for t in range(test_case):
    # 화덕 크기, 피자 개수
    N, M = map(int, input().split())

    cheese = list(map(int, input().split()))

    # 초기설정
    i = 0
    waiting = N                # 웨이팅 중인 피자 인덱스 정보
    pizza_maker = [0] * N      # 화덕
    index_chk = [0] * N        # 화덕에 들어간 인덱스 번호 저장하는 리스트
    last = 0                   # 답

    # 웨이팅 오류 방지
    cheese.append(0)

    # 화덕 생성
    for n in range(N):
        pizza_maker[n] = cheese[n]
        index_chk[n] = n

    while True:

        # 치즈 녹이기
        pizza_maker[i] //= 2

        i += 1

        # 화덕 크기 만큼반 반복
        if i == N:
            i = 0

        # 피자가 다 익으면 웨이팅 중인 피자로 교체
        if pizza_maker[i] == 0:
            pizza_maker[i] = cheese[waiting]
            index_chk[i] = waiting
            waiting += 1

            # 인덱스 오류 방지 //
            if waiting >= M:
                waiting = M

        # 하나 남으면 종료
        if pizza_maker.count(0) == N - 1 and waiting == M:
            break

    # 덜 익은 피자 찾기
    for j in range(N):
        if pizza_maker[j] != 0:
            last = index_chk[j] + 1

    print(f'#{t+1} {last}')