import sys
from collections import deque
sys.stdin = open('input.txt')

"""
1. 확산
2. 공청기 작동
"""
# air1
dys = [0, -1, 0, 1]
dxs = [1, 0, -1, 0]
# air2
dys2 = [0, 1, 0, -1]
dxs2 = [1, 0, -1, 0]
def air_wind(air1, air2):
    y, x = air1, 1
    temp = room[y][x]

    y2, x2 = air2, 1
    temp2 = room[y2][x2]

    for d in range(4):
        # air 1
        while True:
            if 0 <= y + dys[d] < R and 0 <= x + dxs[d] < C:
                next_temp = room[y + dys[d]][x + dxs[d]]
                room[y + dys[d]][x + dxs[d]] = temp
                temp = next_temp


                x += dxs[d]
                y += dys[d]
                # print(y, x, next_temp, temp)
                if y == air1 and x == 0:
                    room[y][x] = -1
                    break
            else:
                room[air1][1] = 0
                break

        # air 2
        while True:
            if 0 <= y2 + dys2[d] < R and 0 <= x2 + dxs2[d] < C:
                next_temp2 = room[y2 + dys2[d]][x2 + dxs2[d]]
                room[y2 + dys2[d]][x2 + dxs2[d]] = temp2
                temp2 = next_temp2

                x2 += dxs2[d]
                y2 += dys2[d]
                if y2 == air2 and x2 == 0:
                    room[y2][x2] = -1
                    break

            else:
                room[air2][1] = 0
                break



def spread():
    next_room = [[0] * C for _ in range(R)]
    for r in range(R):
        for c in range(C):
            if room[r][c] == 0 or room[r][c] == -1:
                continue

            # 미세먼지가 있으면 확산된다
            for d in range(4):
                dr = r + dys[d]
                dc = c + dxs[d]
                # 범위 안에 있고, 공청기가 없는 곳이라면
                if 0 <= dr < R and 0 <= dc < C and room[dr][dc] != -1:
                    next_room[dr][dc] += room[r][c] // 5
                    next_room[r][c] -= room[r][c] // 5
    calc_room(next_room)

def calc_room(list):
    for r in range(R):
        for c in range(C):
            room[r][c] += list[r][c]




R, C, T = map(int, input().split())
room = [list(map(int, input().split())) for _ in range(R)]

# 공청기 찾기 (윗행 아래행과 두칸 이상 떨어져 있다)
air = 2
while True:
    if room[air][0] == -1:
        air1 = air
        air2 = air + 1
        break

    air += 1

for t in range(T):
    spread()
    # for r in room:
    #     print(*r)
    # print('-' * 50)
    air_wind(air1, air2)
    # for r in room:
    #     print(*r)
    # print('-' * 50)

result = 0
for r in range(R):
    for c in range(C):
        result += room[r][c]

print(result + 2)