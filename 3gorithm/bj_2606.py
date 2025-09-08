"""
1. 연결된 네트워크 리스트 만들기
- 한 컴퓨터에 최대로 연결될 수 있는 네트워크의 수는 N-1
"""

stack = []
visit = set()
cnt = 0

# dfs 
def dfs(virus):
    global cnt
    visit.add(virus)
    while True:
        if network[0][virus] == 0:
            if stack:
                virus = stack.pop()
                
            else:
                break
        else:
            visit.add(network[0][virus])
            # 연결된 컴퓨터가 한개 이상일 경우 찾는 for문
            for j in range(1, len(network)):
                if network[j][virus] != 0:
                    stack.append(network[j][virus])
                else:
                    break
            virus = network[0][virus]
        print(virus)
    print(visit)        


# 컴퓨터의 수
N = int(input())

# 컴퓨터 쌍의 수
conect = int(input())

network = [[0] * (N + 1) for i in range(N-1)]
for c in range(conect):
    a, b = map(int, input().split())

    # 네트워크 연결 정보 저장
    j = 0
    while True:
        if network[j][a] != 0:
            j += 1
        else:
            network[j][a] = b
            break

dfs(1)
print(cnt)