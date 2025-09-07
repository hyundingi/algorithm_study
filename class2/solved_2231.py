import sys
N = int(sys.stdin.readline())


result = 0
for i in range(1, 10):
    a = i * 100
    for j in range(1, 10):
        b = j * 10
        for k in range(1, 10):
            c = k
            if N - i - j - k == a+b+c:
                result = a+b+c
                break
    
    if result != 0:
        break

print(result)