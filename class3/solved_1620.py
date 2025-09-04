N, M = map(int, input().split())

pkm_list = [0]
pkm_dict = {}

for n in range(N):
    pkm = input()
    pkm_list.append(pkm)
    pkm_dict[pkm] = n + 1

for _ in range(M):
    a = input()
    if a.isdigit():
        print(pkm_list[int(a)])
    else:
        print(pkm_dict[a])

