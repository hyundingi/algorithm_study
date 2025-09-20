import sys
sys.stdin = open('input2.txt')

def recur(cnt, total, plus, minus, mul, div):
    global min_result, max_result
    if cnt == N:
        min_result = min(min_result, total)
        max_result = max(max_result, total)
        return

    if plus > 0:
        recur(cnt + 1, total + numbers[cnt], plus - 1, minus, mul, div)

    if minus > 0:
        recur(cnt + 1, total - numbers[cnt], plus, minus - 1, mul, div)

    if mul > 0:
        recur(cnt + 1, total * numbers[cnt], plus, minus, mul-1, div)

    if div > 0:
        recur(cnt + 1, int(total / numbers[cnt]), plus, minus, mul, div-1)


T = int(input())
for t in range(T):
    N = int(input())
    oper = list(map(int, input().split()))
    numbers = list(map(int, input().split()))
    min_result = 1e9
    max_result = -1e9

    # cnt, total, +, -, *, /
    recur(1, numbers[0], oper[0], oper[1], oper[2], oper[3])

    print(f'#{t+1} {max_result - min_result}')