import sys
sys.stdin = open('input.txt')


N = int(input())
nums = list(map(int, input().split()))
# + - * /
operator = list(map(int, input().split()))

min_total = 1e9
max_total = -1e9

def dfs(idx, total, plus, minus, multi, div):
    global min_total, max_total

    if idx >= N:
        min_total = min(total, min_total)
        max_total = max(total, max_total)

    if plus > 0:
        dfs(idx+1, total + nums[idx], plus-1, minus, multi, div)

    if minus > 0:
        dfs(idx+1, total - nums[idx], plus, minus-1, multi, div)

    if multi > 0:
        dfs(idx+1, total * nums[idx], plus, minus, multi - 1, div)

    if div > 0:
        dfs(idx+1, int(total / nums[idx]), plus, minus, multi, div-1)


# 최댓값, 최솟값 출력
dfs(1, nums[0], operator[0], operator[1], operator[2], operator[3])
print(max_total)
print(min_total)