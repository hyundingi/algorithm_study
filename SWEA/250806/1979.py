# test case
# T = int(input())

N, K = map(int, input().split())

# 흰 1 검 0
area = [list(map(int, input().split())) for _ in range(N)]

word_ok = 0
for i in range(N):

    # 가로
    for j in range(N - (K+1)):
        count = 0
        for k in range(K):

            if area[i][j+k] == 1:
                count += 1

        if count == K:
            count = 0
            word_ok += 1

            print(j)
            print(k)
            if j+K == N:
                pass

            elif area[i][j+K+1] == 1:
                word_ok -= 1
    # 세로
    for j in range(N - (K+1)):
        count = 0
        for k in range(K):

            if area[j][i+k] == 1:
                count += 1

        if count == K:
            count = 0
            word_ok += 1

            if j + K == N:
                pass

            elif area[j][i + K + 1] == 1:
                word_ok -= 1

print(word_ok)



