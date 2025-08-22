# test_case = int(input())
N = int(input())

# 시작점 찾기 함수
def find_start(N):
    for i in range(N):
        for j in range(N):
            if maze[i][j] == 2:
                return i, j

def bfs(i, j, N):
    # 방문 리스트 생성
    visited = [[0] * N for _ in range(N)]
    # 큐 생성 후 , 방문한 곳 큐에 넣기
    q = [[i, j]]
    # 방문 체크
    visited[i][j] = 1
    while q:
        ti, tj = q.pop(0)
        if maze[ti][tj] == 3:
            return visited[ti][tj] - 2
        for di, dj in [[0, 1], [1, 0], [0, -1], [-1, 0]]:
            wi, wj = ti + di, tj + dj
            if 0 <= wi < N and 0 <= wj < N and maze[wi][wj] != 1 and visited[wi][wj]:
                q.append([wi, wj])
                visited[wi][wj] = visited[ti][tj] + 1


maze = [list(map(int, input().split())) for _ in range(N)]

# 시작점 찾기 함수 호출
sti, stj = find_start(N)
ans = bfs(sti, stj, N)
print(ans)



