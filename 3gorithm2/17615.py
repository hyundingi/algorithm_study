import sys
sys.stdin = open('input.txt')

N = int(input())
balls = input()

count = []

# 빨간공 왼쪽으로 모으기
left_red = balls.lstrip('R')
count.append(left_red.count('R'))

# 빨간공 오른쪽으로 모으기
right_red = balls.rstrip('R')
count.append(right_red.count('R'))

# 파란공 왼쪽으로 모으기
left_blue = balls.rstrip('B')
count.append(left_blue.count('B'))

# 파란공 오른쪽으로 모으기
right_blue = balls.rstrip('B')
count.append(right_blue.count('B'))

print(min(count))