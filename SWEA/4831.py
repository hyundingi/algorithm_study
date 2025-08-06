# 버스는 0번에서 출발해 N번 정류장까지 이동한다
# 한번 충전으로 이동할 수 있는 거리 k
# 충전기가 설치된 정류장의 개수 M개



# test case
T = int(input())

for t in range(T):
    # 이동거리, 정류장 수, 충전기 개수
    K, N, M = map(int, input().split())

    # 정류장 리스트
    bus_stop = [0] * N

    # 충전기가 설치된 정류장 번호
    charge = list(map(int, input().split()))

    for i in range(M):
        # 충전기가 있는 버스 정류장에 1 할당
        bus_stop[charge[i]] += 1

    charge_cnt = 0
    now_stop = 0

    while now_stop < N:
        for j in range(K, 0, -1):

            # 현재 위치에서 K 위치에 충전소가 있는지 확인
            if bus_stop[now_stop+j] == 1:
                now_stop += j
                charge_cnt += 1
                break

            # K부터 다 돌았는데도 충전소가 없으면
            elif j == 1:
                # 강제 종료
                charge_cnt = 0
                now_stop = N + 1

        # 종점 도착
        if now_stop + K >= N:
            break

    print(f'#{t+1} {charge_cnt}')

