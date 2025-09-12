import sys
sys.stdin = open("input.txt")

# 북 동 남 서
dys = [1, 0, -1, 0]
dxs = [0, 1, 0, -1]

def recur(y, x, num):
    # 7글자가 되면 끝
    if len(num) == 7:
        result.add(num)
        return

    if y > 3 or y < 0:
        return

    # 현재 위치 파라미터 값으로 보내야함
    # 델타 값 더해서 보내야ㅕ함
    # 밑에 수정
    recur(y-1, x-1, num + arr[y][x])
    recur(y+1, x+1, num + arr[y][x])

T = int(input())
for t in range(T):
    arr = [list(input().split()) for _ in range(4)]
    num = ''
    result = set()
    recur(0, 0, num)
    print(*result)
    print(len(result))

