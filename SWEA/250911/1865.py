"""
직원들 번호 1 - N
할 일 번호 1 - N

i번 직원이 j번 일을 하면 성공할 확률 P, j

가장 높은 확률 조합 찾기(재귀)
자릿수가 겹치지 않는 숫자 조합을 만든다
"""

# 퍼센테이지 계산 함수
def calc_per(list):
    calc = 1
    for i in range(len(list)):
        calc *= list[i]

    return calc * 100

def recur(row, multi):
    global result
    if row == N:
        # path 의 합이 가장 큰 것이 확률이 제일 좋은 것
        result = max(result, multi)
        return

    # 확률이 낮아지면 return
    # 확률은 어쩌피 곱할수록 줄어든다. 
    # -> 현재곱이 최대 값보다 작으면 곱해봣자 큰 수가 나올 수 없다
    if multi <= result:
        return

    for i in range(N):
        if visited[i] == 1:
            continue
        path.append(works[row][i] / 100)
        visited[i] = 1
        calc = calc_per(path)
        recur(row + 1, calc)
        path.pop()
        visited[i] = 0



T = int(input())
for t in range(T):
    N = int(input())
    works = [list(map(int, input().split())) for _ in range(N)]

    # 저장용
    path = []
    # 방문 기록용
    visited = [0] * N
    # 가장 확률 좋은 거 기록용
    result = 0

    recur(0, 1)

    print(f'#{t+1} {result:.6f}')
