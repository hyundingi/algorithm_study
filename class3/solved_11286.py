import sys
sys.stdin = open('input.txt')
import heapq

heap = []

N = int(sys.stdin.readline())

for n in range(N):
    num = int(sys.stdin.readline())

    if num == 0:
        if heap:
            heapq.heappop(heap)
            print()
        else:
            print(0)
        
        continue

    heapq.heappush(heap, num)