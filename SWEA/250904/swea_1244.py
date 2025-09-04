path, result = set(), []
arr_str = ''
def recur(arr_str):
    if len(arr_str) == len(arr):
        result.append(arr_str)
        print(*result)
        return

    for i in range(len(arr)):
        path.add(arr[i])
        recur(arr_str + arr[i])
        for j in range(len(arr)):
            if arr[j] in path:
                continue
            path.add(arr[j])
            path.remove(arr[j])
        path.remove(arr[i])







T = int(input())
arr, n = input().split()


recur('')