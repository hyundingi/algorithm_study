"""
최소한의 교환횟수로 목적지까지 가는 전기버스
N, N-1 개의 정류장별 배터리 용량
"""

T = int(input())
for t in range(T):
    bus_stop = list(map(int, input().split()))

    now = 1
    count = 0
    while now <= bus_stop[0]:
        elec = bus_stop[now]
        # 이 전기로 끝까지 갈 수 있나?
        if now + elec >= bus_stop[0]:
            break

        # 못가면 충전할 곳 찾아보기
        else:
            max_now = go = 0
            for e in range(1, elec+1):
                # 가장 많이 충전할 수 있는 곳 = 가장 멀리 갈 수 있는 곳인지?
                if max_now < bus_stop[now+e] + (now+e):
                    max_now = bus_stop[now+e] + (now+e)
                    go = e
            count += 1

        now += go

    print(f'#{t+1} {count}')
