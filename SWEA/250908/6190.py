T = int(input())

for t in range(T):
    N = int(input())

    arr = list(map(int, input().split()))

    result = max_result = -1
    multi_list = []
    for i in range(N):
        for j in range(i + 1, N):
            # 곱의 값을 저장
            multi_list.append(arr[i] * arr[j])

    # 값이 단조증가하는 수인지 확인
    for m in range(len(multi_list)):

        # 맥스값보다 작으면 볼 필요 없음 (가지치기)
        if 0 < multi_list[m] < max_result:
            continue

        # 문자로 바꿔서 한글자씩 비교
        str_num = str(multi_list[m])
        for i in range(len(str_num) - 1):
            if str_num[i] <= str_num[i + 1]:
                result = int(str_num)
                continue

            result = -1
            break

        # 단조증가하는 수가 나왔으면 멈춘다
        if result > max_result:
            max_result = result

    print(f'#{t + 1} {max_result}')