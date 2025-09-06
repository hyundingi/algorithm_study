t, n = map(int, input().split())

arr = list(map(int, input().split()))
map_arr = [[0] * 100 for _ in range(2)]
visited = [[0] * 100 for _ in range(2)]

# 트리구조로 만들기
# 최대 두개의 갈림길
for i in range(0, n, 2):
    if map_arr[0][arr[i]] == 0:
        map_arr[0][arr[i]] = arr[i+1]
    else:
        map_arr[1][arr[i]] = arr[i+1]

# 돌아갈 길 저장
back_root=  []
j = 0
while True:
    if map_arr[0][j] == 99:
        print(f'#{t} 1')
        break
    elif map_arr[0][j] != 0:
        now = map_arr[0][j]

        if map_arr[1][j] != 0:
            back_root.append(map_arr[1][j])

    if now == 0:
        now = map_arr[0][back_root.pop()]

    print(back_root)
    j = now


        


            




