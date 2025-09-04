import sys
sys.stdin = open('input.txt')

# 16진수 -> 2진수 dictionary
hex_to_bin = {
    '0': [0, 0, 0, 0],
    '1': [0, 0, 0, 1],
    '2': [0, 0, 1, 0],
    '3': [0, 0, 1, 1],
    '4': [0, 1, 0, 0],
    '5': [0, 1, 0, 1],
    '6': [0, 1, 1, 0],
    '7': [0, 1, 1, 1],
    '8': [1, 0, 0, 0],
    '9': [1, 0, 0, 1],
    'A': [1, 0, 1, 0],
    'B': [1, 0, 1, 1],
    'C': [1, 1, 0, 0],
    'D': [1, 1, 0, 1],
    'E': [1, 1, 1, 0],
    'F': [1, 1, 1, 1],
}

# 앞쪽 0을 생략한 암호 코드
passcode_dict = {
    (2, 1, 1): 0,
    (2, 2, 1): 1,
    (1, 2, 2): 2,
    (4, 1, 1): 3,
    (1, 3, 2): 4,
    (2, 3, 1): 5,
    (1, 1, 4): 6,
    (3, 1, 2): 7,
    (2, 1, 3): 8,
    (1, 1, 2): 9,
}


# 검증하기
def define_code(code):
    total = 0
    for i in range(len(code)-1, -1, -1):
        # 마지막 코드일 때
        if i == 0:
            total += code[i]
            if total % 10 == 0:
                return sum(code)
            else:
                return 0
        # 짝수일ㄸ ㅐ
        elif i % 2 == 0:
            total += code[i]
        # 홀수일 때
        else:
            total += code[i] * 3


tests = int(input())
for test_case in range(1, tests + 1):
    n, m = map(int, input().split())
    arr = [[] for _ in range(n)]
    result = 0
    # n줄의 입력을 받으면서
    for i in range(n):
        temp = input()
        # 각 글자를 0과 1로 변환하며 arr[i]에 추가해준다
        for j in range(m):
            arr[i].extend(hex_to_bin[temp[j]])

    for row in range(n):
        # 뒤에서부터 한글자씩 확인
        idx = m * 4 - 1
        # 뒤에서부터 봤을 때 최소 56글자는 확보가 가능한 동안에 반복 검색
        while idx > 54:
            # 1을 만나면 검증을 시작하는데 ,
            # 만약 위쪽 줄이 0이 아니면
            # 직전 줄에서 이미 확인한 코드임을 알 수 있다
            if not (arr[row][idx] == 1 and arr[row-1][idx] == 0):
                idx -= 1
                continue

            # 비밀번호 만들기
            password = []
            # 비밀번호는 총 8글자
            for _ in range(8):
                # 0과 1이 얼마나 등장했는지
                c2 = c3 = c4 = 0

                # 직전 숫자의 0을 스킵한다
                while arr[row][idx] == 0:
                    idx -= 1
                # 이번 숫자의 4번째 1의 갯수를 찾는다
                while arr[row][idx] == 1:
                    idx -= 1
                    c4 += 1
                # 이번 숫자의 3번째 0의 갯수를 찾는다
                while arr[row][idx] == 0:
                    idx -= 1
                    c3 += 1
                # 이번 숫자의 2번째 1의 갯수를 찾는다
                while arr[row][idx] == 1:
                    idx -= 1
                    c2 += 1

                # 배율을 찾는다.
                ratio = min(c2, c3, c4)
                # 암호에 추가한다.
                password.append(passcode_dict[(c2 // ratio, c3 // ratio, c4 // ratio)])

            result += define_code(password)

            # 암호 찾았으면 앞으로
            idx -= 1
    print(test_case, result)
