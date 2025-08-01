numbers = list(map(int, input().split()))

sum = 0
for number in numbers:
    multi = number ** 2
    sum += multi

vaild = sum%10
print(vaild)