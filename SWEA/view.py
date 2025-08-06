for t in range(10):
    N = int(input())
    buildings_list = list(map(int, input().split()))

    sum_view = 0

    for i in range(N):

        # 뷰가 보이는 빌딩의 값을 리스트에 넣음
        view_list = []

        # 해당 빌딩이 0이상 인지
        if buildings_list[i] > 0:

            # 좌우로 두칸이기 때문에 2번 반복함
            for j in range(1, 3):

                # 오른쪽으로 두개가 해당 빌딩보다 작은 경우
                if buildings_list[i] > buildings_list[i+j]:
                    view = buildings_list[i] - buildings_list[i+j]
                    view_list.append(view)

                # 왼쪽으로 두개가 해당 빌딩보다 작은 경우
                if buildings_list[i] > buildings_list[i-j]:
                    view = buildings_list[i] - buildings_list[i-j]
                    view_list.append(view)

        # 리스트에 값이 4개라는 것은 양쪽으로 두개의 빌딩이 해당 빌딩보다 작다는 것
        if len(view_list) == 4:
            view = min(view_list)
            # 조망권을 가진 빌딩층 합 구하기
            sum_view += view


    print(f'#{t+1} {sum_view}')
