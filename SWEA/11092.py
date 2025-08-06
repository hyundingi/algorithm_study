# test case
T = int(input())

for t in range(T):
    # 양수의 개수
    N = int(input())

    # 양수 N개 리스트
    arr = list(map(int, input().split()))

    min_index = 0
    max_index = 0

    for i in range(N):
        if arr[i] >= arr[max_index]:
            max_index = i

        if arr[i] < arr[min_index]:
            min_index = i

    print(f'#{t+1} {abs(max_index - min_index)}')
