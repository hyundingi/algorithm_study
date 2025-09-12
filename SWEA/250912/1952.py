import sys
sys.stdin = open("input.txt")

T = int(input())

def recur(m, total):
    global result
    # 12월까지 다 돌아보면 끝
    # 가장 금액이 적은 것을 저장한다
    if m > 12:
        result = min(total, result)
        return

    # 12월 까지 안 갔는데 토탈이 이미 min 값을 넘으면 끝
    if total > result:
        return

    # 일일권, 한달권, 세달권, 일년권을 사용했을 경우를 알아본다
    recur(m+1, total + monthly[m] * day)
    recur(m+1, total + month)
    recur(m+3, total + month3)

for t in range(T):
    day, month, month3, year = map(int, input().split())
    monthly = [0] + list(map(int, input().split()))
    # 기준을 일년치로 설정
    result = year

    recur(1, 0)
    print(f'#{t+1} {result}')


