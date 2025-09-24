import sys
sys.setrecursionlimit(10**6)

# 상 하 좌 우
dys = [-1, 1, 0, 0]
dxs = [0, 0, -1, 1]

def dfs(y, x):
    # 이미 계산된 값이 있으면 그걸 그대로 return
    if dp[y][x] > 1:
        return dp[y][x]

    for d in range(4):
        dy = y + dys[d]
        dx = x + dxs[d]

        # 주변을 돌면서 나보다 큰 값을 찾는다
        # 그 큰 값의 주변의 큰 값 + 1 하며 나온 값을 dp 에 저장한다
        if 0 <= dy < n and 0 <= dx < n and forest[y][x] < forest[dy][dx]:
            dp[y][x] = max(dp[y][x], dfs(dy, dx) + 1)

    return dp[y][x] 

n = int(input())
forest = [list(map(int, input().split())) for _ in range(n)]
dp = [[1] * n for _ in range(n)]

result = 0
for y in range(n):
    for x in range(n):
        result = max(dfs(y, x), result)

print(result)