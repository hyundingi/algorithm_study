num_dict = {
    "ZRO":0, 
    "ONE":1, 
    "TWO":2, 
    "THR":3, 
    "FOR":4, 
    "FIV":5, 
    "SIX":6, 
    "SVN":7, 
    "EGT":8, 
    "NIN":9
}

num_count = [0] * 10
num_list = []


T = int(input())
for _ in range(T):
    test_case, numbers = input().split()
    num_list = input().split()

    for num in num_list:
        num_count[num_dict[num]] += 1
    
    for n, i in num_dict:
        print(f'{n * num_list[i]}', end=' ')
