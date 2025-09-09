"""
1. 연결된 네트워크 리스트 만들기
- 한 컴퓨터에 최대로 연결될 수 있는 네트워크의 수는 N-1
"""


# dfs 
def dfs(virus):
    # 제일 첫번째 바이러스 추가
    while True:
        if network[virus]:
            # 방문한 네트워크 visit에 추가
            visit[virus] = 1
            # 연결된 컴퓨터가 한개 이상일 경우 찾는 for문
            # stack에 저장해놓고 0을 만났을 때 pop할거임
            for j in range(1, len(network[virus])):
                stack.append(network[virus][j])

            virus = network[virus][0]
        # 연결된 네트워크가 없으면
        #  stack 에 있는 값을 꺼내 다시 시작
        else:
            visit[virus] = 1
            if stack:
                virus = stack.pop()
            else:
                break
        


# 컴퓨터의 수
N = int(input())

# 컴퓨터 쌍의 수
conect = int(input())
# 네트워크 연결 정보 저장
network = [[] for i in range(N + 1)]
# 연결된 네트워크가 한개 이상일 때 정보 저장
stack = []
# 방문 여부 저장
visit = [0] * (N + 1)

for c in range(conect):
    a, b = map(int, input().split())

    # 네트워크 연결 정보 저장
    network[a].append(b)

print(network)

dfs(1)
print(visit)
print(visit.count(1))