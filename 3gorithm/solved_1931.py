N = int(input())
times = []

# 회의 시간 저장
for _ in range(N):
    start, end = map(int, input().split())
    times.append((start, end))

# 회의 시간 정렬
times = sorted(times, key=lambda x:(x[1],x[0]))

start, end = times[0][0], times[0][1]
cnt = 1

for i in range(1, N):
    if times[i][0] >= end:
        start = times[i][0]
        end = times[i][1]
        cnt += 1

print(cnt)