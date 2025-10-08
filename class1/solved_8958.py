T = int(input())

for t in range(T):
    solved = input()
    cnt = result = 0
    for s in solved:
        if s == 'O':
            cnt += 1
            result += cnt
        elif s == 'X':
            cnt = 0
    
    print(result)