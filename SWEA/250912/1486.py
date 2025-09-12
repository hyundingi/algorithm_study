import sys
sys.stdin = open("input.txt")

T = int(input())

def recur(total, cnt):
    global result
    # 값이 B보다 큰 것 중에 가장 작은 수
    if total >= B:
        result = min(total, result)
        return

    # 직원들 다 돌았을 경우
    if cnt == N:
        return

    # 이미 합이 result 보다 큰 경우
    if total >= result:
        return

    # 포함 시키는 경우
    recur(total + heights[cnt-1], cnt + 1)
    # 포함 안 시키는 경우
    recur(total, cnt + 1)


for t in range(T):
    N, B = map(int, input().split())
    heights = list(map(int, input().split()))
    result = 100000 * N
    recur(0, 0)

    print(f'#{t+1} {result - B}')
