import sys
T = int(sys.stdin.readline())


def fibonachi(num):
    global count_zero, count_one
    dp = [0] * (num + 1)
    dp[0], dp[1] = 0, 1
    for i in range(2, num+1):
        dp[i] = dp[i-2] + dp[i-1]

        if i % 2 == 0:
            count_zero += 1
            count_one +=1 
        elif i % 2 == 1:
            count_one += 2
            count_zero += 1
            
    return dp[num]


for t in range(T):
    N = int(sys.stdin.readline())
    count_zero = count_one = 0
    fibonachi(N)

    print(f'{count_zero} {count_one}')