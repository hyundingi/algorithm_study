def quick_sort(arr, start, end):
    if start >= end:
        return

    pivot = start
    left = start + 1
    right = end

    while left < right:

        # left가 피벗보다 작으면 계속 전진
        while arr[left] <= pivot and left <= right:
            left += 1
        # right 가 피벗보다 크면 계속 전진
        while arr[right] > pivot and left <= right:
            right -= 1
        if left < right:
            # 전진하다가 교환할 거 있으면 함
            arr[left], arr[right] = arr[right], arr[left]

    # 정렬이 끝나면 피벗과 교환
    if left >= right:
        arr[right], arr[pivot] = arr[pivot], arr[right]

    print(arr, pivot)
    # 피벗을 기준으로 두개로 나눠짐
    quick_sort(arr, start, right - 1)
    quick_sort(arr, right+1, end)


T = int(input())
N = int(input())
arr = list(map(int, input().split()))

quick_sort(arr, 0, N - 1)
print(arr)

# -----------------------------------------------------------
# def hoare_partition1(left, right):
#     pivot = arr[left]  # 피벗을 제일 왼쪽 요소로 설정
#     i = left + 1
#     j = right
# 
#     while i <= j:  # 교차가 되면 끝
#         while i <= j and arr[i] <= pivot:  # i 는 pivot 보다 큰 값을 검색 (작거나 같으면 i += 1)
#             i += 1
# 
#         while i <= j and arr[j] >= pivot:  # j 는 pivot 보다 작은 값을 검색 (크거나 같으면 j -= 1)
#             j -= 1
# 
#         if i < j:  # swap
#             arr[i], arr[j] = arr[j], arr[i]
# 
#     # pivot 과 j 위치를 swap
#     arr[left], arr[j] = arr[j], arr[left]
#     return j
# 
# 
# def quick_sort(left, right):
#     if left < right:
#         pivot = hoare_partition1(left, right)
#         # pivot = hoare_partition2(left, right)
#         # pivot = hoare_partition3(left, right)
#         quick_sort(left, pivot - 1)
#         quick_sort(pivot + 1, right)
# 
# N = int(input())
# arr = list(map(int, input().split()))
# quick_sort(0, len(arr) - 1)
# print(arr)



