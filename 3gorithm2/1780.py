import sys
sys.stdin = open('input.txt')

sys.setrecursionlimit(10**6)

cnt1, cnt_1, cnt0 = 0, 0, 0

# 모두 같은 수인지 검사함
def valid(x, y, size):
    for i in range(size):
        for j in range(size):
            if paper[y][x] != paper[y+i][x+j]:
                return False
    return True

# 9등분 한다
def divide(x, y, size):
    global cnt1, cnt0, cnt_1

    # 재귀 종료 조건
    if valid(x, y, size):
        if paper[y][x] == 0:
            cnt0 += 1
        elif paper[y][x] == 1:
            cnt1 += 1
        elif paper[y][x] == -1:
            cnt_1 += 1
        return

    new = size // 3
    for new_y in range(3):
        for new_x in range(3):
            divide(x + new_x * new, y + new_y * new, new)

N = int(input())
paper = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
divide(0, 0, N)

print(cnt_1)
print(cnt0)
print(cnt1)