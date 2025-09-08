T = int(input())

# 베이비진인지 확인하는 함수
def babygin(list):
    cnt = 0
    for i in range(10):
        # 트리플인 경우
        if list[i] == 3:
            return 1
        # 런인 경우 - 1이 연속되면 카운트 +1 함
        elif list[i] >= 1:
            cnt += 1
            # 3이되면 런이다
            if cnt == 3:
                return 1
        # 0이 나오면 카운트 초기화
        else:
            cnt = 0
    # 여기까지 오게 되면 런도 트리플도 없다
    return 0


for t in range(T):
    card_list = list(map(int, input().split()))
    player1, player2 = [0] * 10, [0] * 10

    for i in range(len(card_list)):
        # player 1
        if i % 2 == 0:
            player1[card_list[i]] += 1
            # player 1이 받은 카드 숫자가 3이상이 되었으면 babygin이 됐는지 확인한다
            if i >= 4:
                result = babygin(player1)
                if result:
                    print(f'#{t+1} 1')
                    break
        # player 2
        else:
            player2[card_list[i]] += 1
            # player 2가 받은 카드 숫자가 3이상이 되었으면 babygin이 됐는지 확인한다
            if i >= 4:
                result = babygin(player2)
                if result:
                    print(f'#{t+1} 2')
                    break

    if result == 0:
        print(f'#{t+1} 0')

