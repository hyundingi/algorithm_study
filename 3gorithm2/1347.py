import sys
sys.stdin = open('input.txt')

move = int(input())
dirs = input()
# 상 우 하 좌
dys = [-1, 0, 1, 0]
dxs = [0, 1, 0, -1]
idx = 2

now_y, now_x = 0, 0
min_y, min_x = 0, 0
max_y, max_x = 0, 0

path = [(0, 0),]
width, height = 0, 0

for dir in dirs:
    if dir == 'R':
        idx = (idx + 1) % 4

    elif dir == 'L':
        idx = (idx - 1) % 4

    elif dir == 'F':
        idx %= 4
        now_y += dys[idx]
        now_x += dxs[idx]
        path.append((now_y, now_x))

        min_y = min(min_y, now_y)
        min_x = min(min_x, now_x)
        max_y = max(max_y, now_y)
        max_x = max(max_x, now_x)

height = max_y - min_y + 1
width = max_x - min_x + 1
board = [['#'] * width for _ in range(height)]
for y, x in path:
    board[y - min_y][x - min_x] = '.'

for b in board:
    print(''.join(b))
