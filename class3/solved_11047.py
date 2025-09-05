N, K = map(int, input().split())

coins = [0] * N

for n in range(N-1, -1, -1):
    coins[n] = int(input())

count = 0
for i in range(N):
    if K % coins[i] < K:
        count += K // coins[i]
        K %= coins[i]
        if K == 0:
            break


