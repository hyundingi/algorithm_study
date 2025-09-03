import sys
sys.stdin = open('input.txt')

T = int(input())

for t in range(T):
    # 알파벳별 슛자
    hex_list = {'A':10, 'B':11, 'C':12, 'D':13, 'E':14, 'F':15}
    code_num = ['0001101', '0011001', '0010011', '0111101', '0100011', '0110001', '0101111', '0111011', '0110111', '0001011']

    # 2진수로 변경해줌
    def chg_binary(code):
        binary_code = ''
        bin_list = [0] * 4
        for c in code:
            # 알파벳일 경우 숫자로 10진수 변경해줌
            if not c.isdigit():
                c = hex_list[c]
            num = int(c)
            for i in range(3, 0, -1):
                bin_list[i] = str(num % 2)
                num //= 2
            bin_list[0] = str(num)

            # code에 넣기
            binary_code += ''.join(bin_list)
        return binary_code

    # 암호 푸는 코드
    def solved_code(code):
        real_code = ''
        count = 0
        for i in range(len(code)-1, 0, -1):
            if code[i] == '0':
                count += 1
            else:
                break
        # 코드 뒷자리 0이면 삭제
        code = code[4 - count:len(code) - count]

        # 앞자리 0 갯수세기
        front_cnt = 0
        for i in range(len(code)):
            if code[i] == '0':
                front_cnt += 1
            else:
                break

        # 코드 앞자리 4의 나머지만큼 삭제
        code = code[(front_cnt // 4) * 4:]

        if len(code) > 60:
            code = chg_bin56(code)

        print(code)
        # 이진수를 코드로 바꾸기
        for c in range(len(code) // 7):
            temp = code[c*7:(c*7)+7]
            for i in range(10):
                if code_num[i] == temp:
                    real_code += str(i)
                    break
        return real_code

    # 56자리 이상 이진수 56자리로 변경하는 함수
    def chg_bin56(code):
        # 몇배율인지 확인
        now = code[0]
        min_cnt = 100
        cnt = 0
        for c in range(len(code)):
            if code[c] == now:
                cnt += 1
            else:
                if min_cnt > cnt:
                    min_cnt = cnt
                cnt = 1
                now = code[c]

        now = code[0]
        new_bin = ''
        for c in range(len(code)):
            if code[c] == now:
                cnt += 1
            else:
                new_bin += code[c-1] * (cnt // min_cnt)
                cnt = 1
                now = code[c]
        print('새로 변경')
        return new_bin



    # 검증하기
    def define_code(code):
        total = 0
        result_total = 0
        for i in range(len(code)):
            result_total += int(code[i])
            if i % 2 == 0:
                total += int(code[i]) * 3
            elif i == len(code) - 1:
                total += int(code[i])
                if total % 10 == 0:
                    return result_total
                else:
                    return 0
            else:
                total += int(code[i])

    N, M = map(int, input().split())

    arr = [input() for _ in range(N)]

    secret_code = ''
    temp = 'x'
    result_list = []
    for i in range(N):
        # 뒤에서 부터 찾기
        j = len(arr[i]) - 1
        while True:
            if arr[i][j] != '0':
                if secret_code != arr[i][j-15:j+1]:
                    secret_code = arr[i][j-15:j+1]

                    # 16자리 이상인 경우
                    while True:
                        if arr[i][j-16] != '0':
                            j -= 15
                            if j - 15 < 0:
                                secret_code = arr[i][0:j + 1] + secret_code
                                break
                            else:
                                secret_code = arr[i][j-15:j+1] + secret_code
                        else:
                            break
                    result_list.append(define_code(solved_code(chg_binary(secret_code))))
                j -= 15
            else:
                j -= 1

            if j < 1:
                break
    # print(f'#{t+1} {max(result_list)}')
    print(f'#{t+1} {result_list}')

