
while True:
    test_case = int(input())

    bridge = [input().split() for i in range(100)]

    # 도착 포인트 ~ 출발 포인트 받는 변수
    point_idx = 0

    # 도착 포인트 구하기
    for i in range(100):
        if bridge[99][i] == '2':
            point_idx = i

    # 사다리타기 밑에서 위로 올라감
    for i in range(98, -1, -1):

        # 오른쪽으로 이동 가능 여부 확인
        if point_idx != 99 and bridge[i][point_idx+1] == '1':

            # 연속된 1 세는 함수
            count = 0
            for j in range(point_idx+1, 100):
                if bridge[i][j] == '1':
                    count += 1
                else:
                    break
            
            point_idx += count 
            


        # 왼쪽으로 이동 가능 여부 확인
        elif point_idx != 0 and bridge[i][point_idx-1] == '1':

            # 연속된 1 세는 함수
            count = 0
            for j in range(point_idx-1, -1, -1):
                if bridge[i][j] == '1':
                    count += 1
                else:
                    break
            
            point_idx -= count 

        # 옆으로 이동할 수 없다면 위로 올라감    
        else:
            continue
        

    print(f'#{test_case} {point_idx}')

    if test_case == 10:
        break

        