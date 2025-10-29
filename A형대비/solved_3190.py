import sys
from collections import deque
sys.stdin = open('input.txt')

def chk_d(i):
    if i > 3:
        return 0
    elif i > -1:
        return i
    return 4 + i

def chk_move(y, x):
    if (y, x) in path:
        return True
    if not 0 < y <= N or not 0 < x <= N:
        return True
    return False

def chk_path(y, x):
    global length

    path.append((y, x))
    while len(path) != length:
        path.popleft()

N = int(input())
K = int(input())
grid = [[0] * (N+1) for _ in range(N+1)]
move = deque()
path = deque()

# 사과 위치 정보 저장
for _ in range(K):
    y, x = map(int, input().split())
    grid[y][x] = 1

L = int(input())
for _ in range(L):
    x, c = input().split()
    move.append((int(x), c))

dys = [0, 1, 0, -1]
dxs = [1, 0, -1, 0]

# 초 카운트, 뱀길이, 방향 변경
result, length, d_idx = 0, 1, 0
y, x = 1, 1
game_over = False
s, c = move.popleft()

while True:
    chk_path(y, x)
    result += 1

    y += dys[d_idx]
    x += dxs[d_idx]

    game_over = chk_move(y, x)
    if not 0 < y <= N or not 0 < x <= N:
        game_over = True

    if game_over:
        break

    # print(result, length, y, dys[d_idx], x, dxs[d_idx])
    # 사과 먹기
    if grid[y][x] == 1:
        grid[y][x] = 0
        length += 1

    # 방향 변경하기
    if result == s:
        if c == 'D':
            d_idx += 1
            if move:
                # print(move)
                s, c = move.popleft()

        elif c == 'L':
            d_idx -= 1
            if move:
                # print(move)
                s, c = move.popleft()

        d_idx = chk_d(d_idx)
        # print('dd : ', d_idx)

print(result)