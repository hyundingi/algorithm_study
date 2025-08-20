for t in range(10):
    test_case = int(input())
    my_queue = list(map(int, input().split()))

    # 0이 나올 때까지 반복
    while True:

        # 기본 설정 값 (시작, 마지막, 0번 인덱스에 있는 값 대기공간)
        front = 0
        rear = 7
        temp = 0

        # 사이클
        for i in range(1, 6):
            temp = my_queue[front] - i

            # 앞으로 땡기기
            for j in range(front + 1, 8):
                my_queue[j - 1] = my_queue[j]

            # 종료 조건 (for)
            if temp <= 0:
                my_queue[rear] = 0
                break

            # 앞에 거 제일 뒤로
            my_queue[rear] = temp

        # 종료조건 2 (while)
        if my_queue[rear] <= 0:
            break

    print(f'#{test_case}', end=' ')
    for x in my_queue:
        print(x, end=" ")
    print()
