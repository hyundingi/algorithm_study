"""
1. 연결된 네트워크 리스트 만들기
- 한 컴퓨터에 최대로 연결될 수 있는 네트워크의 수는 N-1
"""
from collections import deque


# dfs
def dfs(virus):
    while q:
        virus = q.popleft()

        # 이미 방문한 적 있으면 pass
        if visit[virus] == 1:
            continue

        # 방문한 적 없으면 방문 표시
        else:
            visit[virus] = 1
            # 순회하며 연결된 네트워크를 찾아 덱에 넣어준다
            for j in range(len(network[virus])):
                # 방문한 적 있는 애면 안 넣음
                if visit[network[virus][j]] == 1:
                    continue

                q.append(network[virus][j])


# 컴퓨터의 수
N = int(input())

# 컴퓨터 쌍의 수
conect = int(input())
# 네트워크 연결 정보 저장
network = [[] for i in range(N + 1)]
# 방문 여부 저장
visit = [0] * (N + 1)

for c in range(conect):
    a, b = map(int, input().split())

    # 네트워크 연결 정보 저장 
    # 꼭 양방향으로 저장해야한다 .. 
    network[a].append(b)
    network[b].append(a)

# 연결된 네트워크가 한개 이상일 때 정보 저장
q = deque([1])
dfs(1)
# 처음 걸린 컴퓨터는 제외한다
print(visit.count(1) - 1)