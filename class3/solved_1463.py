import sys
X = int(sys.stdin.readline())

count = 0
while True:
    if X % 3 == 0:
        count += 1
        X //= 3
    elif X % 3 >= 1:
        count += 1
        X -= 1
    elif X % 2 == 0:
        count += 1
        X //= 2

    if X == 1:
        break

print(count)