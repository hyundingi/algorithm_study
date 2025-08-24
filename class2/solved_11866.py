N, K = map(int, input().split())

arr = [i+1 for i in range(N)]
output = []

k = K-1

while True:

    for i in range(K):
        if i == K-1:
            output.append(arr.pop(0))
        else:
            arr.append(arr.pop(0))
    
    if len(arr) < K:
        for _ in range(len(arr)):
            output.append(arr.pop(0))
        break


# 1 
# 문제점 : K 보다 사람이 적게 남았을 때 해결하지 못함
# while True:

#     # 인덱스 에러 방지
#     # k - 배열길이 = 다시 앞에서부터 찾음
#     if k >= len(arr):
#         k %= len(arr)
    
#     # 두개 남으면 끝
#     if len(arr) == K - 1 :
#         for a in arr:
#             if a > output[-1]:
                

#         for i in range(K-1):
#             a = arr.pop(0)
#             output.append(a)
#         break

#     a = arr.pop(k)
#     output.append(a)

#     k += K - 1


for i in range(N):

    if i == N-1:
        print(f'{output[i]}>', end='')
    
    elif i == 0:
        print(f'<{output[i]}, ', end='')
    
    else:
        print(f'{output[i]}, ', end='')
print()
