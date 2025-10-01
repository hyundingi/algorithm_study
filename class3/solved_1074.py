import sys
# sys.stdin = open('input.txt')
sys.setrecursionlimit(10**6)

N, r, c = map(int, input().split())


def search_part(n, r, c):
    if n == 0:
        return 0

    half = 2 ** (n-1)
    size = half * half

    # 4 사분면
    if r >= half and c >= half:
        return size * 3 + search_part(n-1, r-half, c-half)

    # 3사분면
    if r >= half and c < half:
        return size * 2 + search_part(n-1, r-half, c)
    
    # 2사분면
    if r < half and c >= half:
        return size * 1 + search_part(n-1, r, c-half)
    
    # 1사분면
    if r < half and c < half:
        return search_part(n-1, r, c)


result = search_part(N, r, c)
print(result)

