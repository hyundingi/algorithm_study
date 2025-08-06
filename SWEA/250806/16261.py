# test case
T = int(input())

for t in range(T):
    arr = [int(a) for a in input().split()]

    # 합이 0이 되는 것이 있는지 확인하기 위함
    count = 0

    # arr을 두번 순회함
    for a in arr:
        for b in arr:

            # 합이 0이 있으면 카운트 +1 / 후 break - 순회 횟수를 줄이기 위함
            if a + b == 0:
                count += 1
                break

    if count > 0:
        print(f'#{t+1} 1')
    else:
        print(f'#{t+1} 0')

