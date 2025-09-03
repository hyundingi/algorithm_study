N, x = map(int, input().split())
arr = list(map(int, input().split()))

for n in range(N):
    if arr[n] < x:
        print(arr[n], end=' ')
    