N = int(input())

# 정확하게 가져갈 수 없으면 -1
result = -1

# 3 짜리 설탕이 몇개 필요한지
for i in range((N // 3) + 1):
    # 5 짜리 설탕이 몇개 필요한지
    for j in range((N // 5) + 1):
        # 정확히 N개가 나오면 break
        if (3 * i) + (5 * j) == N:
            result = i + j
            break
    
    # break 해서 나온 값이 최적의 값이기 때문에 바로 끝냄
    if result != -1:
        break

print(result)