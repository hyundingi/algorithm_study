t = int(input())

input_list = [input() for _ in range(t)]

for i in range(t):
    stack = []
    result = "YES"
    for j in input_list[i]:
        if j == "(":
            stack.append(j)
        elif j == ")":
            if stack:
                stack.pop()
            else:
                result = "NO"
    
    if len(stack) != 0:
        result = "NO"
    
    print(result)

            
    


