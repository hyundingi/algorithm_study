import sys
N, M = map(int, sys.stdin.readline().split())
arr = {}

for n in range(N):
    domain, pw = sys.stdin.readline().split()

    arr[domain] = pw

for m in range(M):
    find_domain = input()

    if arr[find_domain]:
        print(arr[find_domain])