T = int(input())

for t in range(T):
    N, M = map(int, input().split())

    containers = list(map(int, input().split()))
    trucks = list(map(int, input().split()))

    # 컨테이너와 트럭을 무게수대로 sort
    containers.sort(reverse=True)
    trucks.sort(reverse=True)

    result, start = 0, 0
    # 트럭에 컨테이너가 들어가면 넣고 아니면 pass
    for m in range(M):
        for n in range(start, N):
            if trucks[m] >= containers[n]:
                result += containers[n]
                start = n + 1
                break

        if start == N:
            break

    print(f'#{t+1} {result}')