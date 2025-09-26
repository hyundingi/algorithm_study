import sys
sys.stdin = open('input.txt')
import heapq

heap = []

N = int(input())
for n in range(N):
    
    num = int(input())

    if num == 0:
        if heap:
            print(-heapq.heappop(heap))
        else:
            print(0)
        
        continue

    heapq.heappush(heap, -num)
