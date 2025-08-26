import sys
# sys.setrecursionlimit(10**6)  # 재귀 제한 완화

n = int(sys.stdin.readline())

arr = [int(sys.stdin.readline()) for _ in range(n)]

# 퀵정렬 
# - low : 피벗 다음부터 시작
# - high : 배열 가장 마지막부터 시작
# - low 가 앞으로 가며 피벗보다 큰 값이 있으면 멈춘다.
# - high가 움직이며 pivot보다 작은 값이 있으면 둘 값을 변경한다.
# - 다시 low가 움직인다 ... 
# - low와 high가 같은점에서 만나게 되거나 서로를 지나치면 1차 정렬 마무리
#  1차 정렬이 끝나면 피벗을 high와 교환


arr.sort()

for a in arr:
    print(a)



# 파이썬으로 퀵정렬 구현
# def quick_sort(arr, start, end):

#     # start 가 end 보다 커지면 비교할 수가 없다는 뜻임
#     if start >= end:
#         return 

#     pivot = start
#     low = start + 1
#     high = end

#     # 1차 정렬 (low > high) 반복
#     while low <= high:

#         # low 가 피벗보다 작으면 계속 전진
#         while low <= end and arr[low] <= arr[pivot]:
#             low += 1
        
#         # high가 피벗보다 크면 계속 전진
#         while high > start and arr[high] >= arr[pivot]:
#             high -= 1

#         # 정렬이 끝났을 때 피벗과 교환
#         if low >= high:
#             arr[high], arr[pivot] = arr[pivot], arr[high]

#         # 중간에 가다가 크거나 / 작은 걸 발견했을 때 교환
#         # 비벗보다 큰 low, 비벗보다 작은 high 교환
#         else:
#             arr[low], arr[high] = arr[high], arr[low]


#         # 두개로 나눠진 피벗 
#         # 왼쪽구간
#         quick_sort(arr, start, high - 1)
#         # 오른쪽 구간
#         quick_sort(arr, high + 1, end)

# quick_sort(arr, 0, n - 1)

# for a in arr:
#     print(a)

# 파이썬으로 퀵정렬 구현 - 2
# 시간 초과 / 메모리 초과 남
# def quick_sort(arr):

#     # arr의 길이가 1보다 작거나 같으면 arr 출력
#     # 1일 경우에 출력되는 것들이 정렬되어 출력됨
#     if len(arr) <= 1:
#         return arr
    
#     # 피벗설정
#     pivot = arr[0]

#     # 피벗보다 작은 거, 큰 거
#     low_nums, high_nums, equal_num = [], [], []
    
#     for num in arr:
#         if pivot > num:
#             low_nums.append(num)
        
#         elif pivot < num:
#             high_nums.append(num)
        
#         else:
#             equal_num.append(num)

#     return quick_sort(low_nums) + quick_sort(equal_num) + quick_sort(high_nums)


# q_sort = quick_sort(arr)

# for q in q_sort:
#     print(q)


