import sys
sys.stdin = open('input.txt')

# 팀 나누기
def recur(idx):
    if idx >= N and visited.count(True) == N // 2:
        calc(visited)
        return

    for i in range(idx, N):
        if visited[i]:
            continue
        visited[i] = True
        recur(i+1)
        visited[i] = False

def calc(list):
    global result
    stark_team = 0
    link_team = 0

    for i in range(N):
        for j in range(N):
            if list[i] and list[j]:
                stark_team += S[i][j]

            elif not list[i] and not list[j]:
                link_team += S[i][j]

    if result > abs(stark_team - link_team):
        result = abs(stark_team - link_team)

N = int(input())
S = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
visited = [False] * N
result = 100 * N // 2

recur(0)
print(result)