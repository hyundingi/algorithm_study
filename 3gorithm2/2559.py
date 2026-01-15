import sys
sys.stdin = open('input.txt')

# 전체 날짜 수 , 연속일자
N, K = map(int, input().split())
temps = list(map(int, input().split()))
# print(temps)
sum, max_sum = 0, -float('inf')
for n in range(N):
    # 가능한 마지막 조합이면 멈춤
    if n + K > N:
        break

    # 처음만 구간만큼 구함
    if n == 0:
        for k in range(K):
            sum += temps[n+k]
    else:
        sum -= temps[n - 1]
        sum += temps[n+K-1]

    if sum > max_sum:
        max_sum = sum

print(max_sum)