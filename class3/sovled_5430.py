from collections import deque
import sys
sys.stdin = open('input.txt')

T = int(input())
for t in range(T):
    p = list(input())
    n = int(input())
    n_arr = input()

    if n != 0:
        n_arr = n_arr.replace('[','').replace(']','').replace(',','')
    print(n_arr)
    deleted = [0] * n
    calc(p)
