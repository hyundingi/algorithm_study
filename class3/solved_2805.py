import sys
sys.stdin = open('input.txt')

def cut_tree():
    length = trees[0]
    cnt = result = 0
    
    while True:            
        cnt += 1

        for i in range(N):
            if result >= M:
                break 

            if trees[i] >= length:
                result += 1
        
        if result >= M:
            break

        length -= 1
    
    return trees[0] - cnt



# 한 줄의 나무 개수 / 필요한 나무 양
N, M = map(int, input().split())
trees = list(map(int, input().split()))

trees.sort(reverse=True)
print(trees)
result = cut_tree()

print(result)
