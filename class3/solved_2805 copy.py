import sys
sys.stdin = open('input.txt')

# 큰 나무 순으로 정렬 후 돌면서 값 구함
def cut_tree_detail(idx, result):
    print(idx, result)

    if result > M:
        return trees[idx] - M

    # (필요한 나무 길이 - 지금까지 자른 나무 길이 ) // 나무수
    total = ((M - result) // (idx))
            
    if total == 0:
        total = ((M - result) % idx)
    
    # 정확하게 안 떨어지면 하나 더 크게
    if trees[idx-1] - total < M:
        return trees[idx-1] - total + 1
    
    else:
        return trees[idx-1] - total



def cut_tree():
    total = result = 0

    for i in range(1, N):
        
        if result == M:
            return trees[i-1]

        total = (trees[i-1] - trees[i]) * i
        
        # 다음 나무 길이 만큼 잘랐을 때 길다면
        # 지금 나무와 다음 나무 사이의 값으로 잘라야함
        if total + result > M:
            return cut_tree_detail(i, result)

        result += total
        
        print('result : ',result)
    
    if result == 0: 
        cnt = 0
        while result >= M:
            cnt += 1
            for i in range(N):
                if result >= M:
                    break
                result += 1
    
    return trees[0] - cnt





# 한 줄의 나무 개수 / 필요한 나무 양
N, M = map(int, input().split())
trees = list(map(int, input().split()))
total = 0

trees.sort(reverse=True)
print(trees)
if N > 1:
    result = cut_tree()
else:
    result = trees[0] - M

print(result)
