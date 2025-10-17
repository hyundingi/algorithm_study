T = int(input())
for t in range(T):
    N = int(input())
    closet_dict = {}

    # 옷장에 딕셔너리 형태로 저장
    for n in range(N):
        a, b = input().split()

        if closet_dict.get(b):
            closet_dict[b] += 1
        else:
            closet_dict[b] = 1

    result = 1
    for a, b in closet_dict.items():
        result *= (b+1)

    print(result - 1)