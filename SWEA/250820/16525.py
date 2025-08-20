test_case = int(input())

for t in range(test_case):
    N, M = map(int, input().split())

    arr = list(map(int, input().split()))

    index = M % N

    print(f'#{t+1} {arr[index]}')