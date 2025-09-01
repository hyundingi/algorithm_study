import math

n = int(input())

arr = list(map(int, input().split()))

count = 0
for i in range(n):
    # 소수 : 1과 자기 자신을 제외하면 자연수 중에 어떤 숫자로도
    # 나누어 떨어지지 않는 숫자
    # 2 미만은 소수 아님
    if arr[i] < 2:
        continue

    else:
        # 숫자의 제곱근을 구한다 
        # 제곱근이란 해당 숫자 루트
        if arr[i] == 3:
            count += 1
            continue
        elif arr[i] == 2:
            count += 1
            continue

        is_prime = True
        for j in range(2, int(math.sqrt(arr[i]) + 1)):
            # 제곱근 까지의 수를 나눴을 때 나눠지는게 있다면 소수가 아니다
            if arr[i] % j == 0:
                is_prime = False
                break

        if is_prime:
            count += 1

print(count)

