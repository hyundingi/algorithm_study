import sys
import heapq
sys.stdin = open('input.txt')

N = int(input())
area = list(map(int, input().split()))
M = int(input())

heap = []
for n in range(N):
    heapq.heappush(heap, area[n])

# 요청대로 모두 배정 가능하다면
# 배정된 예산들 중 최댓값 출력
if sum(area) <= M:
    print(max(area))

else:
    