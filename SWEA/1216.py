for _ in range(10):
    test_case = int(input())

    arr = [list(input().strip()) for _ in range(100)]

    # 들어온 리스트가 회문인지 확인하는 함수
    def check_reverse(list):
        global count
        count = 0 
        for i in range(len(list) // 2):
            if list[i] == list[len(list)-1-i]:
                count += 1
            else:
                break
        
        if count == len(list) // 2:
            return len(list)
        else:
            return 0


    # 회문의 범위
    max_count = 0
    # 가로
    for i in range(100):
        # 범위를 될 수 있는 가장 크게 설정하고 하나씩 줄여감
        idx_range = 100
        flag = 1
        while flag:
            for j in range(101 - idx_range):

                # 리스트를 생성해서 함수에 담아 호출
                check_list = arr[i][j:idx_range+j]
                a = check_reverse(check_list)

                # a가 회문이면 max_count와 비교하고, while문 종료 > 다음 줄로 넘어감
                if a != 0:
                    if a > max_count:
                        max_count = a
                    flag = 0
            
            # 계속 범위를 줄여나감
            idx_range -= 1
            
            # 범위가 0이되면 종료 후 다음 줄로 넘어감
            if idx_range < 1:
                break
        
    # 세로
    for i in range(100):
        idx_range = 100
        flag = 1
        while flag:
            for j in range(101 - idx_range):
                check_list = []

                # 함수에 태워보낼 리스트를 생성함
                for k in range(idx_range):
                    check_list.append(arr[k+j][i])
                a = check_reverse(check_list)
                
                # a가 회문이면 max_count와 비교하고, while문 종료 > 다음 줄로 넘어감
                if a != 0:
                    if a > max_count:
                        max_count = a
                    flag = 0
            
            # 계속 범위 줄임
            idx_range -= 1
            
            # 범위가 0이 되면 종료 후 다음 줄로 넘어감
            if idx_range < 1:
                break


    print(f'#{test_case} {max_count}')

        