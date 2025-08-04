S = input()

# 소문자 리스트
lower = [chr(i) for i in range(97, 123)]

# -1 이 소문자 개수만큼 들어간 리스트 생성
alpha_list = [-1] * len(lower)

# 글자 수 만큼 순회
for s in range(len(S)):

    # 소문자 개수만큼 순회 하며 같은 문자가 있는지 확인
    for i in range(len(lower)):

        # 같다면 s의 인덱스 번호를 리스트에 추가
        if S[s] == lower[i]:
            if alpha_list[i] == -1:
                alpha_list[i] = s

for a in alpha_list:
    print(a, end=' ')




