import sys
sys.stdin = open('input.txt')
"""
1. 벨트 회전
2. 가장 먼저 벨트에 올라간 로봇부터 회전하는 방향으로 한 칸 이동할 수 있으면 함
    - 로봇을 올리거나 로봇이 이동한 칸이면 내구도 1 감소
3. 로봇 올리기 (내구도 > 0)
4. 내구도가 0인 칸의 개수가 k개 이상이면 종료
"""

N, K = map(int, input().split())
dura = list(map(int, input().split()))
robot = [0] * N
count = 0
while dura.count(0) < K:
    # 1. 벨트 회전
    temp = dura.pop()
    dura = [temp] + dura
    temp = robot.pop()
    robot = [temp] + robot

    # 로봇 N에 도착했으면 내리기
    if robot[N-1] == 1:
        robot[N-1] = 0

    # 로봇 이동
    if robot.count(1) > 0:
        for i in range(N-2, -1, -1):
            if robot[i] == 1 and robot[i+1] == 0 and dura[i+1] > 0:
                robot[i], robot[i + 1] = 0, 1
                dura[i+1] -= 1

    # 로봇 N에 도착했으면 내리기
    if robot[N-1] == 1:
        robot[N-1] = 0

    # 로봇 올리기
    if dura[0] > 0:
        robot[0] = 1
        dura[0] -= 1


    print(robot)
    print(dura)
    print('-'*10)
    count += 1

print(count)
