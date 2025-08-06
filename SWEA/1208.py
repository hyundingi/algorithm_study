# 가장 큰 수 -1 , 가장 작은 수 +1
# 제한하는 횟수만큼 반복

for t in range(10):
    dump = int(input())
    boxes = list(map(int, input().split()))

    max_index = 0
    min_index = 0

    # 덤프 수 만큼 반복
    while dump > 0:

        for d in range(100):
            if boxes[max_index] < boxes[d]:
                max_index = d

            if boxes[min_index] > boxes[d]:
                min_index = d

        # max 는 -1 /  min 은 +1
        boxes[max_index] -= 1
        boxes[min_index] += 1

        dump -= 1

    # 한번더 찾기
    for d in range(100):
        if boxes[max_index] < boxes[d]:
            max_index = d

        if boxes[min_index] > boxes[d]:
            min_index = d

    print(f'#{t + 1} {boxes[max_index] - boxes[min_index]}')

