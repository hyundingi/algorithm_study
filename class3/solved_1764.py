N, M = map(int, input().split())

not_famous_dict = {}

for _ in range(N):
    name = input()
    not_famous_dict[name] = 1

# trash = input()

not_famous_list = []
for _ in range(M):
    name = input()
    # .get() 을 하면 키값이 존재할 때 키의 밸류값 반환 / 없으면 None 반환
    # 딕셔너리를 생성할 때 밸류값을 1로 설정해놔서 True가 되기 때문에 출력됨
    if not_famous_dict.get(name):
        not_famous_list.append(name)

print(len(not_famous_list))
not_famous_list = sorted(not_famous_list)
for name in not_famous_list:
    print(name)
