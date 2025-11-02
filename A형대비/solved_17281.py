import sys
sys.stdin = open('input.txt')

def score(tajas):
    t, total = 0, 0
    for n in range(N):
        out = 0
        b1, b2, b3 = 0,0,0
        
        while out <  3:
            p = tajas[t]
            
            if player[n][p] == 0:
                out += 1
            
            elif player[n][p] == 1:
                total += b3
                b3, b2, b1 = b2, b1, 1
            
            elif player[n][p] == 2:
                total += b3 + b2
                b3, b2, b1 = b1, 1, 0
            
            elif player[n][p] == 3:
                total += b3 + b2 + b1
                b3, b2, b1 = 1, 0, 0
            
            elif player[n][p] == 4:
                total += b3 + b2 + b1 + 1
                b1, b2, b3 = 0, 0, 0
            
            t = (t + 1) % 9
    return total

def recur(idx):
    global max_total
    if idx == 9:
        total = score(tajas)
        max_total = max(total, max_total)
        return

    # 4번 타자는 이미 채워져있기 때문에 return
    if idx == 3:
        recur(idx + 1)
        return 

    # 선수 조합 생성    
    for i in range(9):
        if visited[i]:
            continue
        tajas[idx] = i
        visited[i] = 1
        recur(idx + 1)
        visited[i] = 0      

N = int(input())
player = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
tajas = [0] * 9
tajas[3] = 0  # 1번 선수 4번 타자 고정

# 순열 중복 방지
visited = [0] * 9
visited[0] = 1  # 1번 선수 이미 사용
max_total = 0

recur(0)
print(max_total)
