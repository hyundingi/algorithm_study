import sys
T = int(sys.stdin.readline())


def fibonachi(num):
    global count_zero, count_one

    dp = [[0, 0] for _ in range(num + 1)]

    if num == 0:
        dp[num][0] += 1
    
    elif num == 1:
        dp[num][1] += 1

    else:
        dp[0][0] += 1
        dp[1][1] += 1
        for i in range(2, num+1):
            dp[i][0] = dp[i-2][0] + dp[i-1][0]
            dp[i][1] = dp[i-2][1] + dp[i-1][1]
                
    return dp[num]


for t in range(T):
    N = int(sys.stdin.readline())
    count_zero = count_one = 0
    result = fibonachi(N)

    print(f'{result[0]} {result[1]}')