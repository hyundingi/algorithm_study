T = int(input())

for t in range(T):
    N = int(input())

    boxes = list(map(int, input().split()))

    # max 중력
    max_count = 0
    # 쌓인 상자 개수
    stack_box = 0

    # 상자 개수 만큼 반복
    for box in range(N):
        # 상자 개수 만큼 반복하여 하나하나 비교 / 떨어지는 박스 아래에 있는 박스 부터
        for i in range(box+1, N):

            # 쌓이는 박스 개수 세기 (떨어지는 박스와 같거나 , 크면)
            if boxes[box] <= boxes[i]:
                stack_box -= 1
        # 총 개수에서 내 위치 만큼 빼고 쌓인 박스 개수만큼 뺀 것이 max 중력인지 찾기
        if (N - (box - 1)) + stack_box > max_count:
            max_count = (N - (box - 1)) + stack_box

        # 초기화
        stack_box = 0

    print(f'#{t+1} {max_count}')