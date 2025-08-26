import sys
import math

m, n = map(int, sys.stdin.readline().split())

for num in range(m, n + 1):

    # 2미만은 소수 아님
    if num < 2:
        continue

    is_prime = True
    # 2 ~ 제곱근 만큼만 반복 
    # 1 * 36
    # 2 * 18
    # 3 * 12
    # 4 * 9
    # 6 * 6  ← 여기서부터 약수가 뒤집힘
    # 9 * 4
    # 12 * 3
    # 18 * 2
    # 36 * 1
    # 꼭 int로 바꿔줄 것
    for i in range(2, int((math.sqrt(num))) + 1):

        if num % i == 0:
            is_prime = False
            break

    if is_prime:
        print(num)