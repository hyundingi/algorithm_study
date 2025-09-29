import sys
sys.setrecursionlimit(10**6)

N, r, c = map(int, input().split())


# 2 n-1 로 4 등분힘 > 4등분의 끝을 만나면 다음으로 넘어감

#왼위, 오위, 왼아, 오아
dys = [0, 0, 1, 1]
dxs = [0, 1, 0, 1]
memo = [[0] * (2 ** (N-1)) for _ in range(2 ** (N-1))]

y = x = 0
cnt = 0
 
for i in range(y, 2 ** (N-1), 2):
    for j in range(x, 2 ** (N-1), 2):

        for d in range(4):
            dy = i + dys[d]
            dx = j + dxs[d]

            if dy == r and dx == c:
                continue

            memo[dy][dx] = cnt 
            cnt += 1
            
print(memo)