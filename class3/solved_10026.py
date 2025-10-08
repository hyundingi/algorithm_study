import sys
sys.stdin = open('input.txt')

N = int(input())
colors = [list(input()) for _ in range(N)]

# 북 동 남 서
dys = [-1, 0, 1, 0]
dxs = [0, 1, 0, -1]

for y in range(N):
    for x in range(N):
        colors[y][x]
    