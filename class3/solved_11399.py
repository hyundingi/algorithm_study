N = int(input())
P_arr = list(map(int, input().split()))

total = 0

P_arr = sorted(P_arr)

for n in range(N):
    total += P_arr[n]
    if n == 0:
        continue
    else:
        for nn in range(n):
            total += P_arr[nn]


print(total)