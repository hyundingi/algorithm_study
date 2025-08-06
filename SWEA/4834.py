#1.
# test case
T = int(input())

for t in range(T):
    # 카드 장수
    N = int(input())

    # 카드 번호 리스트로 받기
    cards = list(map(int, input()))

    # 숫자의 범위 만큼 count 리스트 생성
    counts = [0] * 10

    # 개수 세기
    for i in range(N):
        counts[cards[i]] += 1

    max_count = 0
    max_num = 0

    # len(counts) - 1 == 9 / len(counts) 로 하면 인덱스 에러남
    # 똑같은 장수의 카드가 있을 때 큰 수를 출력하기 위해 역순으로 range
    for i in range(9, 0, -1):
        if counts[i] > max_count:
            max_count = counts[i]
            max_num = i

    print(f'#{t+1} {max_num} {max_count}')
