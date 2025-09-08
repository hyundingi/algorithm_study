T = int(input())

# 두장의 카드를 골라서 교환하는 함수
# 교환 횟수만큼 교환을 할건데,
# 일단 함수에서 한번 교환한 다음
# 횟수가 남아있으면 횟수를 줄이고 재귀호출하는 형태로 구현
def swap(chg):
    # 교환 횟수가 내가 주어진 교환 횟수가 되었을 때
    if chg == n:
        # 내가 알고있는 최댓값과 비교한다.
        global max_prize
        # 현재 카드의 상태를 바탕으로 상금 만들기
        prize = int(''.join(cards))
        if max_prize < prize:
            max_prize = prize
        return 0

    # 두장의 카드를 고른다
    for i in range(len(cards) - 1):
        for j in range(i + 1, len(cards)):
            cards[i], cards[j] = cards[j], cards[i]
            # 방금 만든 숫자가 만든적 있던 숫자인지?
            local_prize = int(''.join(cards))
            if local_prize not in path[chg]:
                path[chg].add(local_prize)
                # 없으먼 다음 교환 진행
                swap(chg + 1)
            # 원복 시킨다.
            # 다음 노드에서도 같은 card 상태에서 진행해야하기 때문에
            cards[j], cards[i] = cards[i], cards[j]


for t in range(T):
    cards, n = input().split()
    cards = list(cards)
    n = int(n)
    # 몇번째 교환에서 어떤 숫자가 나왔는지를 기록함
    # path[i] : i번 교환했을 때 본 적 있는 숫자들의 집합
    path = [set() for _ in range(n)]
    max_prize = 0
    swap(0)
    print(f'#{t+1} {max_prize}')



# ---------------------------------------------------
# path, result = set(), []
# arr_str = ''
# def recur(arr_str):
#     if len(arr_str) == len(arr):
#         result.append(arr_str)
#         print(*result)
#         return

#     for i in range(len(arr)):
#         path.add(arr[i])
#         recur(arr_str + arr[i])
#         for j in range(len(arr)):
#             if arr[j] in path:
#                 continue
#             path.add(arr[j])
#             path.remove(arr[j])
#         path.remove(arr[i])


# T = int(input())
# arr, n = input().split()

# recur('')
# ---------------------------------------
# path, num_arr = [], []
# def recur(cnt):
#     if cnt == chg:
#         print(*path)
#         return 0

#     for i in range(len(nums)):
#         for j in range(i+1, len(nums)):
#             num_arr[i], num_arr[j] = num_arr[j], num_arr[i]
#             path.append(num_arr)


# T = int(input())
# nums, chg = input().split()
# num_arr.extend(nums)

# recur(0)


