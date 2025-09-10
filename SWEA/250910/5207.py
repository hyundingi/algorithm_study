# 1. 서로 다른 정수 N개 정렬 후 A에 저장
# 2. B에 저장된 M개의 정수가
# 3. A에 들어 있는 수인지 탐색
# 4. 탐색 과정에서 양쪽구간을 번갈아 선택하게 되는 숫자의 개수

T = int(input())
N, M = map(int, input().split())
A = sorted(list(map(int, input().split())))
B = list(map(int, input().split()))

start, end = 0, len(A)
while True:
    mid = (start+end) // 2
    for b in B:
        if A[mid] > b:
            start = 0
            end = mid - 1
            
        elif A[mid] == b:
            break
        break
        
           

