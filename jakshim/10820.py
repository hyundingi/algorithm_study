import sys

data = sys.stdin.read().splitlines()

for line in data:

    if line:
        # 문자열에 포함되어 있는 소문자, 대문자, 숫자, 공백의 개수 구하기
        small_cnt = big_cnt = number_cnt = space_cnt = 0

        number = [str(i) for i in range(10)]

        # N을 하나씩 순회
        for n in line:

            # 만약 n이 공백이면,
            if n == ' ':
                space_cnt += 1

            # 숫자이면
            elif n in number:
                number_cnt += 1

            # 만약 n의 타입이 문자이면,
            elif type(n) == str:

                # n이 소문자인지
                if str.islower(n):
                    small_cnt += 1

                # n이 대문자인지
                elif str.isupper(n):
                    big_cnt += 1

        print(f'{small_cnt} {big_cnt} {number_cnt} {space_cnt}')



