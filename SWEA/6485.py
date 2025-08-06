# i 번째 버스 노선은 번호가 A 이상 B  이하인 모든 정류징만을 다니는 버스 노선
# P개의 버스 정류자ㅣㅇ에 대해 각 정류장에 몇 개의 버스 노선이 다니는지

# test case
T = int(input())

for t in range(T):
    # n 개의 버스
    N = int(input())

    # N개의 버스 노선을 담은 2차 배열
    arr = [list(map(int, input().split())) for n in range(N)]

    # P개의 버스 정류장
    P = int(input())

    # 정류장 번호
    P_arr = [int(input()) for p in range(P)]

    # 정류장 몇 번 지나는지 개수 세는 리스트
    counts = [0] * 5000

    # 버스 노선 만큼 반복
    for a in arr:
        # A ~ B count + 1
        for i in range(a[0]-1, a[1]):
            counts[i] += 1

    print(f'#{t+1}', end=' ')
    for p in P_arr:
        print(counts[p-1], end=' ')
    print()







