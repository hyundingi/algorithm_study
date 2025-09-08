T = int(input())

for t in range(T):
    N = int(input())

    arr = list(map(int, input().split()))

    result = 0
    multi_list = []
    for i in range(N):
        for j in range(i+1, N):
            # 곱의 값을 저장
            multi_list.append(str(arr[i] * arr[j]))

    # 곱한 값을 내림차순 정렬
    multi_list.sort(reverse=True)
    # 값이 단조증가하는 수인지 확인
    for m in range(len(multi_list)):
        for mm in range(len(multi_list[m])-1):
            if multi_list[m][mm] <= multi_list[m][mm+1]:
                result = int(multi_list[m])
                continue
            else:
                result = -1
                break

        # 단조증가하는 수가 나왔으면 멈춘다
        if result > 0:
            break

    print(f'#{t+1} {result}')