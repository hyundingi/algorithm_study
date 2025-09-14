import sys

def recur(step, total):
    global result

    # 마지막 칸을 밟은 것만 계산
    if step > N and visited[N]:
        result = max(total, result)
        return
    
    # 계단 수는 넘었는데 마지막 칸을 안 밟으면 pass
    if step > N:
        return

    # 연속된 세 개의 계단을 올랐을 경우
    if visited[step-1] and visited[step-2]:
        return
    
    

    visited[step] = 1 
    visited[0] = 0
    
    recur(step + 1, total + steps[step])
    recur(step + 2, total + steps[step])

    visited[step] = 0
    paht.pop()
        


N = int(sys.stdin.readline())
steps = [0] + [int(sys.stdin.readline()) for _ in range(N)] 
visited = [0] * (N + 1)

result = 0
recur(0, 0)

print(result)

        
 
        