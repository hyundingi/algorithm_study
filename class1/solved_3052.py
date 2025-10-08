path = [0] * 43
for _ in range(10):
    N = int(input())

    path[N%42] += 1

result = 0
for p in path:
    if p != 0:
        result += 1

if result == 0:
    print(1)
else:
    print(result)

