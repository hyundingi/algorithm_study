import sys
sys.stdin = open('input.txt')

# 마법사 명수
N = int(input())

times = []
min_time, max_time = 0, 0
for n in range(N):
    A, B = map(int, input().split())
    times.append(B - A)

times.sort()

# N이 홀수면 중앙 값이 한 개 밖에 없어서 무조건 1이다
if N % 2 == 1:
    print(1)

else:
    # 중앙의 두 값 사이에 있는 모든 정수가 최소값을 만든다
    print(times[N//2] - times[N//2 - 1] + 1)

