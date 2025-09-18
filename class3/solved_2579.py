import sys
sys.stdin = open("input2.txt")

# 시간 초과 코드
# def recur(step, total):
#     global result
#
#     # 마지막 칸을 밟은 것만 계산
#     if step > N and visited[N]:
#         result = max(total, result)
#         return
#
#     # 계단 수는 넘었는데 마지막 칸을 안 밟으면 pass
#     if step > N:
#         return
#
#     # 연속된 세 개의 계단을 올랐을 경우
#     if visited[step - 1] and visited[step - 2]:
#         return
#
#     visited[step] = 1
#     visited[0] = 0
#
#     recur(step + 1, total + steps[step])
#     recur(step + 2, total + steps[step])
#
#     visited[step] = 0
#     paht.pop()


N = int(sys.stdin.readline())
steps = [0] + [int(sys.stdin.readline()) for _ in range(N)]

# result = 0
# recur(0, 0)

# 계단이 하나밖에 없으면 하나가 끝
if N == 1:
    print(steps[1])

# 계단이 두개밖에 없으면 두개가 끝
elif N == 2:
    print(steps[1] + steps[2])

# 계단이 3개 이상일 때
else:
    dp = [0] * (N + 1)
    dp[1] = steps[1]
    dp[2] = steps[1] + steps[2]
    # 연속된 세개를 밟을 수 없음
    # 가능한 것 - 1번, 3번 밟기 / 2번 3번 밟기
    # 그 중 더 큰 값을 저장함
    dp[3] = max(steps[1] + steps[3], steps[2] + steps[3])

    for i in range(4, N+1):
        # o x o / o x o o
        # 앞에 한칸 밟았는지 / 두칸 밟았는지
        dp[i] = max(dp[i-2] + steps[i], dp[i-3] + steps[i-1] + steps[i])

    print(dp[-1])