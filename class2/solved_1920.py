import sys
n = int(sys.stdin.readline())
arr = set(map(int, sys.stdin.readline().split()))

m = int(sys.stdin.readline())
mrr = list(map(int, sys.stdin.readline().split()))

for i in range(m):
    l = len(arr)
    arr.add(mrr[i])

    if l == len(arr):
        print(1)
    else:
        arr.remove(mrr[i])
        print(0)
    
    


# 시간 초과
# for m_num in mrr:
#     if m_num in arr:
#         print(1)
#     else:
#         print(0)


# 메모리초과
# check_list = [0] * (max_arr + 1)

# for i in range(n):
#     check_list[arr[i]] = 1

# for i in range(m):
#     if mrr[i] > max_arr:
#         print(0)
#     else:
#         print(check_list[mrr[i]])

    

        
