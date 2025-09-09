T = int(input())
for t in range(T):
    a, b, c = map(int, input().split())

    result, eat = 0, 0
    while True:
        # 조건 만족
        if a < b < c:
            print(f'#{t+1} {eat}')
            break

        # 어떤 방식으로 하더라도 안됨
        elif c < 3 or b < 2:
            result = -1
            print(f'#{t+1} -1')
            break

        elif b >= c:
            eat += b - (c - 1)
            b = c - 1

        elif a >= b:
            eat += a - (b - 1)
            a = b - 1

