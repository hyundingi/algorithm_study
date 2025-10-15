import sys
sys.setrecursionlimit(10**6)
sys.stdin = open('input.txt')

"""
1. 가장 왼쪽 계란을 든다
2. 나머지 계란들 중에서 하나를 고른다
3-1. 깨지면 넘어감
3-2. 안 깨졌으면 제자리에 두고 오른쪽에 있는 계란을 든다
4. 가장 오른쪽에 있는 계란이 깨질 경우 종료
"""

def dfs(idx):
    global ans

    if idx == N:
        # 가장 오른쪽 끝까지 왔다면 내구도가 1 이상인 것들을 카운트
        cnt = sum(1 for s, _ in eggs if s <= 0)
        ans = max(ans, cnt)
        return 
    
    
    # 현재 계란이 이미 깨져있는 계란이라면 다음으로
    if eggs[idx][0] <= 0:
        dfs(idx + 1)
        return
    
    # 한번이라도 부딪혔는지 체크용도
    hit_any = False

    for n in range(N):
        # 나 자신이거나 이미 깨진 계란이라면 pass
        if n == idx or eggs[n][0] <= 0:
            continue
        
        # 계란 치기
        hit_any = True
        hit(idx, n)
        dfs(idx + 1)
        back(idx, n) # 초기화
    
    # 부딪힐 계란이 없으면 그냥 다음 계란으로
    if not hit_any:
        dfs(idx + 1)

def hit(idx, next_idx):
    eggs[idx][0] -= eggs[next_idx][1]
    eggs[next_idx][0] -= eggs[idx][1]

def back(idx, next_idx):
    eggs[idx][0] += eggs[next_idx][1]
    eggs[next_idx][0] += eggs[idx][1]



N = int(input())
# s : 내구도
# w : 무게
# 계란이 깨지는 조건 s - w < 0
eggs = [list(map(int, input().split())) for _ in range(N)]
ans = 0

dfs(0)
print(ans)