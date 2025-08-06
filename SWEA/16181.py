# test case
T = int(input())

# T 만큼 반복
for t in range(T):
    # cards
    cards = list(map(int, input().strip()))

    # 번호 수 세는 리스트
    counts = [0] * 10

    # 갯수 세기
    for card in cards:
        counts[card] += 1

    baby_gin = 0
    for a in range(2):
        for i in range(len(counts)):

            # count가 3이상 == triple
            if counts[i] >= 3:

                # 카운트값 빼기
                counts[i] -= 3
                baby_gin += 1

        # 1이 연속되면 run
        for j in range(len(counts)):
            if counts[j] >= 1 and counts[j+1] >= 1 and counts[j+2] >= 1:

                # 카운트값 빼기
                counts[j] -= 1
                counts[j+1] -= 1
                counts[j+2] -= 1
                baby_gin += 1

    if baby_gin == 2:
        print(f'#{t+1} 1')
    else:
        print(f'#{t+1} 0')



