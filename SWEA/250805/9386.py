# test case
T = int(input())

for t in range(T):
    # num
    N = int(input())

    # arr
    arr = list(input())

    count = 0
    max_count = 0

    # 수열의 길이만큼 반복
    for i in range(N):
        # 만약 1이면 count + 1
        if arr[i] == '1':
            count += 1

        # 만약 0이면, 카운트 초기화
        elif arr[i] == '0':
            count = 0

        # 만약 카운트가 맥스 카운트보다 크면 맥스카운트 갱신
        if max_count < count:
            max_count = count

    print(f'#{t+1} {max_count}')
