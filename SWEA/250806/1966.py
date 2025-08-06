# test case
T = int(input())

for t in range(T):
    N = int(input())

    arr = [a for a in list(map(int, input().split()))]

    for i in range(N):
        # N - 1 부터 역순으로 돌림
        for j in range(N - 1, 0, -1):

            # 가장 뒤에 있는게 자기 앞에 있는 것보다 작으면 자리 변경
            if arr[j] < arr[j-1]:
                temp = ''
                temp = arr[j]
                arr[j] = arr[j-1]
                arr[j-1] = temp

    print(arr)

    # 리스트 컴프리헨션
    print(f'#{t+1} {" ".join(str(x) for x in arr)}')