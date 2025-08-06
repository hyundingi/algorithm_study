T = int(input())

for t in range(T):

    # 양수 개수 N개
    N = int(input())
    # 리스트로 받기
    arr = list(map(int, input().split()))

    # 기본값은 첫번째에 있는 값으로 할당
    max_num = arr[0]
    min_num = arr[0]

    # 양수 개수만큼 반복
    for n in range(N):
        if arr[n] > max_num:
            max_num = arr[n]
        elif arr[n] < min_num:
            min_num = arr[n]

    print(f'#{t + 1} {max_num - min_num}')
