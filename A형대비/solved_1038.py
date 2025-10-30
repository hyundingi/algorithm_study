from collections import deque
N = int(input())

if N <= 9:
    print(N)

else:
    q = deque(range(10))
    count = -1
    result = 0

    while q:
        num = q.popleft()
        count += 1

        if count == N:
            result = num
            break

        last_num = num % 10

        for next_num in range(0, last_num):
            q.append(num * 10 + next_num)

    if result == 0:
        print(-1)
    else:
        print(result)

# # 해당 자리수에서 나올 수 있는 가장 큰 감소하는 수 인지 확인
# def chk_num(arr, chk_arr):
#     if arr == chk_arr:
#         return True
#     return False
#
# if 10 < N < 1023:
#     count = 9
#     i = 0
#     while True:
#         # 100으로 나눴을 때 딱 떨어지면 볼 필요 없음
#         if i % 100 == 0:
#             i += 1
#             continue
#
#         arr = list(map(int, str(i)))
#         chk_arr = [i for i in range(len(arr), -1)]
#         for j in range(len(arr)-1):
#             if arr[j] <= arr[j+1]:
#                 # if arr[j+1] != 0:
#                 break
#             if j == len(arr) - 2:
#                 print(i)
#                 count += 1
#
#         if count == N:
#             print(i)
#             break
#
#         if chk_num(arr, chk_arr):
#             temp = 0
#             for n in range(len(arr)+1):
#                 temp += 10**n * len(arr)
#                 i = temp
#         else:
#             i += 1
# elif 10 >= N:
#     print(N)
#
# else:
#     print(-1)


