n = int(input())

delta = [list(map(int, input().split())) for _ in range(n)]

# sorted 는 delta 리스트의 각 요소를 하나씩 꺼내 lambda에 넣음
# lambda (받은 요소) : 필요한 값
sorted_list = sorted(delta, key=lambda dd:(dd[0], dd[1]))

for x, y in sorted_list:
    print(f'{x} {y}')