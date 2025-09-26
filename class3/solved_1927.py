import sys
import heapq
heap = []

N = int(sys.stdin.readline())
for n in range(N):
    num = int(sys.stdin.readline())

    if num == 0:
        if len(heap) == 0:
            print(0)
            continue
        
        print(heapq.heappop(heap))
        continue

    heapq.heappush(heap, num)