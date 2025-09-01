test_case = int(input())

for _ in range(test_case):
    R, S = map(str, input().split())

    r = int(R)

    for i in range(len(S)):
        print(S[i] * r, end='')
    print()



