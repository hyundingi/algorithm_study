import sys
sys.setrecursionlimit(10**6)
sys.stdin = open('input.txt')

def fair(stu):
    global cnt
    visited[stu] = True
    next_node = students[stu]

    # 방문한 적 없다면 다음 노드
    if not visited[next_node]:
        fair(next_node)

    # 방문한 적 있음
    else:
        # 근데 종료되지 않음 (루프)
        if not finished[next_node]:
            # 이 루프에 몇명이 포함되어 있는지 센다
            curr = next_node
            cnt += 1

            while curr != stu:
                curr = students[curr]
                cnt += 1

    finished[stu] = True

T = int(input())

for t in range(T):
    n = int(input())
    students = [0] + list(map(int, sys.stdin.readline().split()))
    # 방문 확인
    visited = [False] * (n + 1)
    # 루프가 끝났는지 확인
    finished = [False] * (n + 1)

    # 팀 매칭에 성공한 인원 수
    cnt = 0
    for i in range(1, n + 1):
        if not visited[i]:
            fair(i)

    print(n - cnt)

