import sys

test_Case = int(sys.stdin.readline())

queue = []

def queue_push(a):
    queue.append(a)

def queue_front():
    if queue:
        print(queue[0])
    else:
        print(-1)

def queue_back():
    if queue:
        print(queue[-1])
    else:
        print(-1)

def queue_pop():
    if queue:
        print(queue.pop(0))
    else:
        print(-1)

def queue_size():
    print(len(queue))

def queue_empty():
    if queue:
        print(0)
    else:
        print(1)


for t in range(test_Case):
    order = sys.stdin.readline().split()

    if order[0] == 'push':
        queue_push(order[1])
    
    elif order[0] == 'front':
        queue_front()
    
    elif order[0] == 'size':
        queue_size()

    elif order[0] == 'pop':
        queue_pop()
    
    elif order[0] == 'empty':
        queue_empty()
    
    elif order[0] == 'back':
        queue_back()
    




