arr = [int(input()) for a in range(9)]

max_num = 0
num_index = 0
for i in range(len(arr)):
    if arr[i] > max_num:
        max_num = arr[i]
        num_index = i+1

print(max_num)
print(num_index)
