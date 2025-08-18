test_case = int(input())

arr = [list(input().strip()) for _ in range(100)]

for i in range(100):
    for j in range(95):

        words = []
        for k in range(5):
            words.append(arr[i][j + k])
        
        reverse_words = words[::-1]
        for k in range(95):

            if arr[i][k:k+5] == reverse_words:
            
                print('있음', k)

