for t in range(10):
    N = int(input())

    infix = input()
    postfix = ''
    stack = []
    top = -1

    level = {'+':1, '*':2}

    # 후위 표기식으로 변경
    for token in infix:
        if token.isdigit():
            postfix += token
        else:
            if top == -1 or level[stack[top]] < level[token]:
                stack.append(token)
                top += 1
            elif level[stack[top]] >= level[token]:
                while top > -1 and level[stack[top]] >= level[token]:
                    postfix += stack.pop()
                    top -= 1
                stack.append(token)
                top += 1

    while True:
        if top != -1:
            postfix += stack.pop()
            top -= 1

        elif top == -1:
            break


    # 후위 표기식 연산
    for token in postfix:
        if token.isdigit():
            stack.append(int(token))

        elif token == '+':
            a = stack.pop()
            b = stack.pop()
            stack.append(a+b)

        elif token == '*':
            a = stack.pop()
            b = stack.pop()
            stack.append(a*b)

    print(f'#{t+1} {stack[0]}')