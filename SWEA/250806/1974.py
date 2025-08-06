# test case
T = int(input())

for t in range(T):

    # 스도쿠 이차배열
    sudoku = [list(map(int, input().split())) for _ in range(9)]

    # 합이 45가 나와야함
    max_sum = 45
    # 스도쿠 완성 여부
    success = 1

    i = 0
    while i < 8:

        total = 0
        for j in range(9):              # 가로줄
            total += sudoku[i][j]

        # 줄의 합이 45가 아니면 실패
        if total != max_sum:
            success = 0
            break

        total = 0
        for j in range(9):              # 세로줄
            total += sudoku[j][i]

        # 줄의 합이 45가 아니면 실패
        if total != max_sum:
            success = 0
            break

        # 9칸짜리 합구하기 i가 0, 3, 6 일때만 실행됨
        if i % 3 == 0:
            # 0이 들어오면 (0,0) , (3,0) , (6, 0) 한 줄을 계산하기 위한 for문
            # 3이 들어오면 (0,3) , (3,3), (6,3) ...
            # 6이 들어오며면 (0,6) , (3, 6) (6,6)
            for j in range(0, 9, 3):
                total = 0
                for c in range(3):
                    for r in range(3):
                        total += sudoku[c+j][i+r]

                if total != max_sum:
                    success = 0
                    break

        i += 1

    if success == 0:
        print(f'#{t+1} 0')
    else:
        print(f'#{t+1} 1')
