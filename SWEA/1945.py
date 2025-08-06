# test case
T = int(input())

for t in range(T):
    # 숫자
    N = int(input())

    multi = [0] * 5

    while True:

        if N % 11 == 0:
            N /= 11
            multi[4] += 1

        elif N % 7 == 0:
            N /= 7
            multi[3] += 1

        elif N % 5 == 0:
            N /= 5
            multi[2] += 1

        elif N % 3 == 0:
            N /= 3
            multi[1] += 1

        elif N % 2 == 0:
            N /= 2
            multi[0] += 1

        else:
            break
    print(f'#{t+1} {multi[0]} {multi[1]} {multi[2]} {multi[3]} {multi[4]}')