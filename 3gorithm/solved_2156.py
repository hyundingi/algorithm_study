import sys
sys.stdin = open('input.txt')

N = int(input())

podos = [int(input()) for _ in range(N)]

# 포도주 잔이 1잔일 때
if N == 1:
    print(podos[0])

# 포도주 잔이 2잔일 때
elif N == 2:
    print(podos[0] + podos[1])

# 포도주 잔이 3잔 이상일 때
else:
    # dp에는 해당 번째에 나올 수 있는 최대의 수를 저장한다.
    dp = [0] * N
    dp[0] = podos[0]
    dp[1] = podos[1] + podos[0]
    # 연속 3잔은 못 마시니까 
    # 첫번째 잔 + 세번째잔 / 두번째잔 + 세번째잔 중 뭐가 더 많이 마실 수 있는지 확인 후 저장한다.
    # O X O / X O O 
    dp[2] = max(podos[0] + podos[2], podos[1] + podos[2], dp[1])

    for i in range(3, N):
        # O X O, O X O O
        # dp[i] = max(dp[i - 2] + podos[i], dp[i - 3] + podos[i - 1] + podos[i])
        # 이번 순서에서 나올 수 있는 경우의 수
        dp[i] = max(
            dp[i - 1], # O X (안마신다)
            dp[i - 2] + podos[i], # O X O (마신다 - 바로 앞 잔을 안 마셨을 경우) 
            dp[i - 3] + podos[i - 1] + podos[i] # O X O O (마신다 - 바로 앞 잔을 마셨을 경우)
        )

    print(dp[-1])


