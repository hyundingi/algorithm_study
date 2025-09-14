def recur(total):
    global cnt
    if total == n:
        cnt += 1
        return
    
    if total > n:
        return
    
    recur(total + 1)
    recur(total + 2)
    recur(total + 3)



T = int(input())
for t in range(T):
    n = int(input())
    cnt = 0
    recur(0)
    print(cnt)