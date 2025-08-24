import sys

test_Case = int(sys.stdin.readline())

stack = []

def stack_push(a):
    stack.append(a)

def stack_top():
    if stack:
        print(stack[-1])
    else:
        print(-1)

def stack_pop():
    if stack:
        print(stack.pop())
    else:
        print(-1)

def stack_size():
    print(len(stack))

def stack_empty():
    if stack:
        print(0)
    else:
        print(1)


for t in range(test_Case):
    order = sys.stdin.readline().split()

    if order[0] == 'push':
        stack_push(order[1])
    
    elif order[0] == 'top':
        stack_top()
    
    elif order[0] == 'size':
        stack_size()

    elif order[0] == 'pop':
        stack_pop()
    
    elif order[0] == 'empty':
        stack_empty()
    




