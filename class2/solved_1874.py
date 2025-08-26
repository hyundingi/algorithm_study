n = int(input())

arr = [int(input()) for _ in range(n)]
# [4, 3, 6, 8, 7, 5, 2, 1]
stack = []

for i in range(n):
    if stack:
        if arr[i] > stack[-1]:
            pass
    else:
        stack.append((arr[i]))
