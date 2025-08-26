import sys

n = int(sys.stdin.readline())
n_arr = list(map(int, sys.stdin.readline().split()))
m = int(sys.stdin.readline())
m_arr = list(map(int, sys.stdin.readline().split()))

count_dict = {}

for num in n_arr:
    if num in count_dict:
        count_dict[num] += 1
    else:
        count_dict[num] = 1

count_list = []

for num in m_arr:
    if num in count_dict:
        count_list.append(str(count_dict[num]))
    else:
        count_list.append('0')


print(' '.join(count_list))