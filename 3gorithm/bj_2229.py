import sys
sys.stdin = open('input.txt')

N = int(input())
scores = list(map(int, input().split()))

# (수도 코드)

dp = [0] * N

for i in range(N):
    # i번째 학생을 기준으로 dp[i]를 계산
    current_max_score = 0  # dp[i]에 들어갈 값을 찾기 위함

    for j in range(i, -1, -1):  # j는 i부터 0까지 거꾸로 순회 (i..i), (i-1..i), ..., (0..i)

        # 1. scores[j...i] 구간의 max와 min을 구합니다.
        # (이 부분은 j가 작아질 때마다 효율적으로 갱신할 수 있습니다)
        current_group_scores = scores[j: i + 1]
        group_score = max(current_group_scores) - min(current_group_scores)

        # 2. '이전까지의 최대 점수'를 가져옵니다.
        #    j=0 이라서 (0~i까지가 한 조) 이전 점수가 없으면 0입니다.
        if j == 0:
            before_score = 0
        else:
            before_score = dp[j - 1]

        # 3. (이전 점수 + 현재 j~i 그룹 점수) 와
        #    지금까지 찾은 dp[i]의 후보(current_max_score) 중 더 큰 값을 선택합니다.
        current_max_score = max(current_max_score, before_score + group_score)

    dp[i] = current_max_score

# 최종 답
print(dp[N - 1])


"""
잘 하는 학생 + 덜 잘하는 학생

나이 차이가 많이 날 경우 오히려 -
1. 나이 순서대로 정렬
2. 적당히 학생들을 나눔 
조의 개수는 상관없다 

잘 짜여진 기준
1. 높은 점수 - 낮은 점수 

전체적으로 잘 짜여진 기준 
잘 짜여진 기준의 합 

조원이 1명이면 0
"""

# scores 몇번째에 있는 수인지
# 조인원 몇명으로 구성할건지
# def calc(i, len):
#     list = scores[i:i+len]
#     return max(list) - min(list)

# def recur(now, total):
#     global max_total
#     if now >= N:
#         max_total = max(total, max_total)
#         return

#     for i in range(now+1, N+1):
#         if matrix[now][i] == 0:
#             continue
#         recur(i, total + matrix[now][i])


# N = int(input())
# scores = list(map(int, input().split()))
# matrix = [[0] * (N+1) for _ in range(N)]

# for n in range(N):
#     matrix[n][0] = scores[n]
#     for k in range(1, N-n+1):
#         if k == 1:
#             matrix[n][k+n] = 0
#         else:
#             matrix[n][k+n] = calc(n, k)

# # for d in matrix:
# #     print(*d)
# # print('-'*10)

# max_total = 0
# recur(0, 0)
# print(max_total)
