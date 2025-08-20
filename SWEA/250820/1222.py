for t in range(10):
    N = int(input())

    infix = input()
    postfix = ''
    stack = []

    # 후위 표기식으로 변경
    for token in infix:
        if token == '+':
            stack.append(token)

        else:
            postfix += token
            if stack:
                postfix += stack.pop()

    # 후위 표기식 연산
    for token in postfix:
        if token != '+':
            stack.append(int(token))

        else:
            a = stack.pop()
            b = stack.pop()

            stack.append(a+b)

    result = stack.pop()
    print(f'#{t+1} {result}')
