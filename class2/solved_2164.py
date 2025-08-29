from collections import deque

n = int(input())

queue = deque([i+1 for i in range(n)])

while len(queue) > 1:

    # 처음 거 하나 버림
    queue.popleft()
    # 다음 거 빼서 뒤에 추가함
    queue.append(queue.popleft())

print(queue[0])

