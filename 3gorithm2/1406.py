import sys
sys.stdin = open('input.txt')

# 입력된 문자열
left_stack = list(sys.stdin.readline().strip())
M = int(sys.stdin.readline())

cursor = len(left_stack)
right_stack = []


for m in range(M):
    order = sys.stdin.readline().split()

    # 커서를 왼쪽으로 한 칸 옮긴다
    if order[0] == 'L':
        if left_stack:
            right_stack.append(left_stack.pop())

    # 커서를 오른쪽으로 한 칸 옮긴다
    elif order[0] == 'D':
        if right_stack:
            left_stack.append(right_stack.pop())

    # 커서 왼쪽에 있는 문자를 삭제한다.
    elif order[0] == 'B':
        if left_stack:
            left_stack.pop()

    # 커서 왼쪽에 문자를 추가한다
    elif order[0] == 'P':
        left_stack.append(order[1])

print(''.join(left_stack) + ''.join(reversed(right_stack)))