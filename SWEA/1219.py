t, n = map(int, input().split())

arr = list(map(int, input().split()))
map_arr = [[0] * 100 for _ in range(2)]

# 트리구조로 만들기
for i in range(0, n, 2):

    if map_arr[0][arr[i]] == 0:
        map_arr[0][arr[i]] = arr[i+1]
    else:
        map_arr[1][arr[i]] = arr[i+1]

for i in range(2):
    for j in range(100):
        if map_arr[i][j] == 99:
            




