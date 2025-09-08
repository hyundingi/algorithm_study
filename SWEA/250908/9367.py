T = int(input())

for t in range(T):
    N = int(input())
    clist = list(map(int, input().split()))
    
    # 최소 길이 1
    count = 1
    maxcount = 0
    for i in range(N-1):
        # 다음 당근이 지금 당근보다 크면 count 
        if clist[i] < clist[i+1]:
            count += 1
        else:
            count = 1

        if maxcount < count:
            maxcount = count

    print(f'#{t+1} {maxcount}')