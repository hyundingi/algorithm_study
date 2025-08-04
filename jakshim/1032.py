N = int(input())

if N > 1:

    file_names = []
    for n in range(N):

        # 파일 이름 한개씩 저장하는 배열 생성
        file_name = [x for x in input()]

        # 2차배열로 만듬
        file_names.append(file_name)

    # 다른 값을 찾는 리스트 생성
    diffrent = [0] * len(file_name)

    # N - 1 만큼 반복
    for n in range(N - 1):

        # 파일 이름의 길이만큼 반복
        for f in range(len(file_name)):

            # 해당 파일 명과 다음 파일 명을 비교 - 다르면 ? / 같으면 문자 넣기
            # 이미 물음표가 된 것은 비교 안 함 
            if diffrent[f] != '?':
                if file_names[n][f] != file_names[n+1][f]:
                    diffrent[f] = '?'
                else:
                    diffrent[f] = file_names[n][f]

    # 배열을 붙여서 출력
    print(''.join(diffrent))

else:
    file_name = input()
    print(file_name)




