N = int(input())
size = list(map(int, input().split()))
t, p = map(int, input().split())

Tcount = 0
for i in range(len(size)):
    if size[i] == 0:
        continue
    # 한 묶음만 주문하면 될 경우
    if size[i] // t == 0:
        Tcount += 1
    
    # 여러묶음 주문해야할경우
    elif size[i] // t > 0:
        # 티 한묶음이랑 딱 떨어질경우
        if size[i] % t == 0:
            Tcount += size[i] // t
        # 안 떨어질 경우
        else:
            Tcount += (size[i] // t) + 1 

print(Tcount)
print(f'{N // p} {N % p}')