import sys
sys.stdin = open('input.txt')

N, M = map(int, input().split())
arr = list(map(int, input().split()))
total_arr = [0] * N

# 누적합 리스트 생성
# 펜윅트리(바이너리 인덱스 트리) 사용






# ----------------------------------------------------
# for i in range(N):
#     if i == 0:
#         total_arr[i] = arr[0]
#     total_arr[i] = total_arr[i-1] + arr[i]


# for i in range(M):
#     result = 0
#     start, end = map(int, input().split())
#     if start == 1:
#         result = total_arr[end-1]

#     else:
#         result = total_arr[end-1] - total_arr[start-2]

#     print(result)