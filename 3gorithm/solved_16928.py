import sys
sys.stdin = open("input.txt")

N, M = map(int, input().split())
board = [0] * 101

# 사다리 정보 저장
for n in range(N):
    start, end = map(int, input().split())
    board[start] = end

# 뱀 정보 저장
for m in range(M):
    start, end = map(int, input().split())
    board[start] = end


def bfs(start):
    while now <= 100:
        max_move = 6
        for i in range(6, 0, -1):
            # 백이 넘으면 그냥 끝
            if now + i >= 100:
                break

            # 사다리 혹은 뱀이 없거나 , 뱀을 만났을 때
            if board[now+i] == 0 or now+i > board[now+i]:
                continue

            # 가장 멀리 가는 사다리 정보 저장
            if board[now+i] > max_move:
                max_move = board[now+i]

        # 사디라가 없으면 6 이동, 사다리가 있으면 사다리만큼 이동
        if max_move > 6:
            now = max_move
        else:
            now += max_move

        count += 1

# -----------------------------
import sys
sys.stdin = open("input.txt")

N, M = map(int, input().split())
board = [0] * 101

# 사다리 정보 저장
for n in range(N):
    start, end = map(int, input().split())
    board[end] = start

# 뱀 정보 저장
for m in range(M):
    start, end = map(int, input().split())
    board[start] = end

# 거꾸로 가자
now, count, dice = 100, 0, 0
while now > 1:

    now -= 1
    count += 1
    print(now)
    print(dice)

    # 일단 6만큼 감
    if count == 6:
        dice += 1
        count = 0

    # 6만큼 왔는데 사다리 혹은 뱀을 만날 경우 처리
    if count == 0:
        if board[now] > 0:
            now = board[now]
            continue
        elif board[now] != 0 and board[now] < now:
            now += 1
            continue

    # 6가기 전에 사다리 만났을 경우
    if board[now] > 0:
        now = board[now]
        print('사다리 ', now)
        count = 0
        dice += 1



print('주사위 ', dice)























