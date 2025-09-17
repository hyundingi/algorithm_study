import sys
sys.stdin = open('input2.txt')

def cook(score, kcal, prev_idx):
   global max_total
   if kcal < L:
       max_total = max(max_total, score)

   if kcal > L:
       return

   for i in range(prev_idx, N):
       if visited[i]:
           continue
       visited[i] = 1
       cook(score + scores[i][0], kcal + scores[i][1], i)
       visited[i] = 0

T = int(input())
for t in range(T):
    N, L = map(int, input().split())
    scores = [list(map(int, input().split())) for _ in range(N)]
    visited = [0] * N
    max_total = 0

    # 점수합, 칼로리 합, 이전에 선택한 재료
    cook(0, 0, 0)
    print(f'#{t+1} {max_total}')