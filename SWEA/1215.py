for t in range(10):
    
    word_len = int(input())

    arr = [list(input().strip()) for _ in range(8)]

    count = 0

    for i in range(8):
        for j in range(8 - word_len + 1):

            # 가로줄
            words_x = []
            # 찾아볼 글자 수 만큼 반복하여 빈 리스트에 담는다
            for k in range(word_len):
                words_x.append(arr[i][j + k])

            # 회문 비교 - 틀리면 0 하고 종료 , 같으면 1
            word_check = 0
            for k in range(word_len // 2):
                compare_word = words_x.pop()
                if words_x[k] != compare_word:
                    word_check = 0
                    break
                else:
                    word_check = 1

            # 회문 갯수 카운트
            count += word_check

            # 세로줄
            words_y = []
            # 찾아볼 글자 수 만큼 반복하여 빈 리스트에 담는다
            for k in range(word_len):
                words_y.append(arr[j + k][i])

            # 회문 비교 - 틀리면 0 하고 종료 , 같으면 1
            word_check = 0
            for k in range(word_len // 2):
                compare_word = words_y.pop()
                if words_y[k] != compare_word:
                    word_check = 0
                    break
                else:
                    word_check = 1

            # 회문 갯수 카운트
            count += word_check

    print(f'#{t+1} {count}')