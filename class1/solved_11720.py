N = int(input())
number_str = input()

numbers = [int(x) for x in number_str]

sum = 0
for number in numbers:
    sum += number

print(sum)