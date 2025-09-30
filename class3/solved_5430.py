
import sys
sys.stdin = open('input.txt')

def calc():
    start, now, last = 0, 0, n-1
    for i in range(len(p)):
        
        if p[i] == 'R':
            if now == start:
                now = last
            else:
                now = start
        
        elif p[i] == 'D':
            if n == 0 or (start > last):
                print('error')
                return
            else:
                if now == start:
                    now += 1
                    start += 1
                else:
                    now -= 1
                    last -= 1
    
    return result(start, now, last)

def result(s, n, l):
    if n == l:
        print('[', end='')
        for i in range(l, s-1, -1):
            if i == s:
                print(n_arr[i], end='')
                continue
            print(n_arr[i], end=',')
        print(']')
    
    elif n == s:
        print('[', end='')
        for i in range(s, l+1):
            if i == l:
                print(n_arr[i], end='')
                continue
            print(n_arr[i], end=',')
        print(']')




T = int(input())
for t in range(T):
    p = list(input())
    n = int(input())
    n_arr = input()

    if n != 0:
        n_arr = list(map(int, n_arr.replace('[','').replace(']','').split(',')))

    calc()
