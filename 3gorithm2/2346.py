import sys
from collections import deque
sys.stdin = open('input.txt')

N = int(input())
moves = list(map(int, sys.stdin.readline().split()))

balloons = deque()
for n in range(N):
    balloons.append((n+1, moves[n]))

result = []

while balloons:
    b, move = balloons.popleft()
    result.append(b)

    if not balloons:
        break

    if move > 0:
        # (move - 1)만큼 왼쪽으로 회전
        balloons.rotate(-(move - 1))
    else:
        balloons.rotate(-move)

print(*result)


