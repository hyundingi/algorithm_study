import sys
from heapq import heappop, heappush
sys.stdin = open('input.txt')

# def bfs():
#     total = 0
#     for n in range(N):
#         hq = []
#         for idx in range(3):
#             heappush(hq, (rgbs[n][idx], idx))
#
#         while hq:
#             length, color = heappop(hq)
#             # 이전에 색칠된 거라면 다음 거 pop
#             if visited[color]:
#                 continue
#             else:
#                 print(length,color)
#                 clear_visited()
#                 total += length
#                 visited[color] = 1
#                 break
#
#     return total
#
# def clear_visited():
#     for i in range(3):
#         visited[i] = 0


N = int(input())
# 빨강, 초록, 파랑
rgbs = [list(map(int, input().split())) for _ in range(N)]
# visited = [0] * 3
# print(bfs())

dp = [[1001 * N] * 3 for _ in range(N)]

dp[0][0] = rgbs[0][0]
dp[0][1] = rgbs[0][1]
dp[0][2] = rgbs[0][2]

for i in range(1, N):
    for j in range(3):

        for k in range(3):
            if j == k:
                continue
            else:
                dp[i][j] = min(dp[i-1][k] + rgbs[i][j], dp[i][j])

print(min(dp[N-1]))



