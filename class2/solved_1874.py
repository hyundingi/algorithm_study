n = int(input())

arr = [int(input()) for _ in range(n)]
# [4, 3, 6, 8, 7, 5, 2, 1]
stack, result_list, result_calc = [], [], []

def push(num):
    stack.append(num)
    result_calc.append('+')

def pop():
    result_list.append(stack.pop())
    result_calc.append('-')

count = 1
i = 0
result = 0
while True:
    
    # pop
    if arr[i] < count:
        pop()
        i += 1    
    
    else:
        # push
        push(count)
        count += 1

    if count > n and len(stack) == 0:

        if result_list == arr:
            result = True
            break
        else:
            result = False
            break

if result:
    for a in result_calc:
        print(a)
else:   
    print('NO')

