import sys

n = int(sys.stdin.readline())

arr = [int(input()) for _ in range(n)]

arr.sort()

for a in arr:
    print(a)


# 시간초과
# arr = [0] * 10001

# for i in range(n):
#     num = int(sys.stdin.readline())
#     arr[num] += 1

# count = 0
# j = 0
# while count < n:
#     if arr[j] != 0:
#         for i in range(arr[j]):
#             count += 1
#             print(j)
    
#     j += 1
