numsize = {
    1: 1,
    2: 10,
    3: 100,
    4: 1000,
    5: 10000,
    6: 100000,
    7: 1000000,
}

def binary_search(min, num):
    left = min
    right = min * 10

    while left <= right:
        mid = (left+right) // 2
        if mid ** 3 > num:
            right = mid - 1
        elif mid ** 3 < num:
            left = mid + 1
        elif mid ** 3 == num:
            return mid

    return -1



T = int(input())

for t in range(T):
    N = input()
    # 숫자 자릿수를 세고 사이즈표에서 맞는 range 범위를 가져온다
    if len(N) % 3 == 0:
        size = len(N) // 3
    else:
        size = (len(N) // 3) + 1

    min_size = numsize[size]
    result = binary_search(min_size, int(N))
    print(f'#{t+1} {result}')
