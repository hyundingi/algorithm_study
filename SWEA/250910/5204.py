# 분할
def merge_sort(arr):
    if len(arr) == 1:
        return arr

    mid = len(arr) // 2
    left = arr[:mid]
    right = arr[mid:]

    # 계속 해서 분할
    left_list = merge_sort(left)
    right_list = merge_sort(right)

    # 분할된 거 정렬
    merge_list = merge(left_list, right_list)
    return merge_list

# 병합
def merge(left, right):
    global cnt
    # 병합된 거 담을 리스트
    result = [0] * (len(left) + len(right))
    # 인덱스 설정
    r = l = 0

    # 오른쪽 마지막 원소보다 왼쪽 마지막 원소가 큰 경우 +1
    if left[-1] > right[-1]:
        cnt += 1

    # l 혹은 r 이 인덱스를 벗어나기 전까지 실행
    while l < len(left) and r < len(right):
        # 작은 거 먼저 넣는다
        if left[l] < right[r]:
            result[l+r] = left[l]
            l += 1
        else:
            result[l+r] = right[r]
            r += 1

    # result에 들어가지 못한 애들 따로 관리
    while l < len(left):
        result[l+r] = left[l]
        l += 1

    while r < len(right):
        result[l+r] = right[r]
        r += 1

    return result






T = int(input())
for t in range(T):
    N = int(input())
    arr = list(map(int, input().split()))
    cnt = 0
    result = merge_sort(arr)
    print(f'#{t+1} {result[len(result) // 2]} {cnt}')