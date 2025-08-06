T = int(input())

for t in range(T):
    # 정수 개수 , 구간 개수
    N, M = map(int,input().split())
    arr = list(map(int, input().split()))

    # 합을 저장하는 리스트 생성
    sum_list = []

    # 합을 받는 변수 생성
    sum = 0

    # indexError를 대비해 range 맞추기
    for n in range(N-(M-1)):

        for m in range(M):
            sum += arr[n+m]

        # 리스트에 추가
        sum_list.append(sum)

        # 초기화
        sum = 0

    # 기본값 할당
    sum_min = sum_list[0]
    sum_max = sum_list[0]

    for s in sum_list:

        if s > sum_max:
            sum_max = s

        elif s < sum_min:
            sum_min = s

    print(f'#{t+1} {sum_max - sum_min}')