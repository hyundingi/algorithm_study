import sys
sys.stdin = open('input.txt')

# 시계수 리스트
def recur(cnt, path):
    if cnt == 4:
        num_list.append(path)
        return

    for i in range (1, 10):
        recur(cnt+1, path+str(i))

# 가장 낮은 시계수 조합 찾기
def find_low():
    path = []
    for i in range(4):
        num = ''.join(map(str, nums[i:] + nums[:i]))
        path.append(num)
    return min(path)

# 입력 받기
nums = list(map(int, input().split()))

num_list = []
recur(0, '')

low_num = find_low()

# 몇번째로 작은 값인지 찾기
for i in range(len(num_list)):
    if num_list[i] == low_num:
        print(i)
        break
