while True:
    arr = list(map(int, input().split()))
    
    if arr.count(0) == 3:
        break
    
    max_num = max(arr)
    idx = arr.index(max_num)

    calc = 0
    for i in range(len(arr)):

        if i == idx:
            continue
        else:
            calc += arr[i] ** 2
        
    
    if arr[idx] ** 2 == calc:
        print('right')
    else:
        print('wrong')
   

    
