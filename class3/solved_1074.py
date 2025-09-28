import sys
sys.setrecursionlimit(10**6)

N, r, c = map(int, input().split())


a = r // 4 
b = r % 4 
aa = c // 4 
bb = c % 4

if N > 2:
    result = (((2 ** N) // 4) * 16 * a) - 1 + (aa * 16 ) + ((b-1) * 4 ) + bb
else:
    result = (((2 ** N) // 4) * 8 * a) - 1 + (aa * 8 ) + ((b-1) * 2 ) + bb

print(result)

# 왼위, 오위, 왼아, 오아
# dys = [0, 0, 1, 1]
# dxs = [0, 1, 0, 1]


# def recur(y, x):
#     global cnt
#     if x == 2 ** N:
#         x = 0
#         y += 4

#     for i in range(y, y + 4, 2):
#         for j in range(x, x + 4, 2):

#             for d in range(4):
#                 dy = i + dys[d]
#                 dx = j + dxs[d]

#                 if dy == r and dx == c:
#                     return 

#                 cnt += 1
        
#     recur(y, x + 4)

            
# cnt = 0
# recur(0, 0)
# print(cnt)