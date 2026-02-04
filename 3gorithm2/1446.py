import sys
sys.stdin = open('input.txt')

N, D = map(int, input().split())
# 지름길 시작, 도착, 지름길 길이
loads = []
for _ in range(N):
    start, end, dist = map(int, input().split())

    # 끝 지점이 목적지를 넘지 않고, 정말 지름길이 맞을 때만 계산
    if end <= D and end - start > dist:
        loads.append((start, end, dist))

dp = [i for i in range(D+1)]

for i in range(D+1):
    # 이전 칸에서 온 거리와 비교
    # 지름길 타고 온 거 or 이전에서 1만큼 앞으로 온 거
    if i > 0:
        dp[i] = min(dp[i], dp[i-1]+1)

    # 현재 시점에서 시작하는 지름길이 있는 지 확인
    for s, e, d in loads:
        if i == s:
            if dp[e] > dp[i] + d:
                dp[e] = dp[i] + d

print(dp[D])