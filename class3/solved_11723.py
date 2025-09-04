import sys
M = int(sys.stdin.readline())

s = set()

def add(num):
    s.add(num)

def remove(num):
    # num이 없는 경우 그냥 넘어감 - discard
    s.discard(num)

def check(num):
    print(1 if num in s else 0)

def toggle(num):
    if num in s:
        s.remove(num)
    else:
        s.add(num)

def all():
    s.clear()
    for i in range(1, 21):
        s.add(i)

def empty():
    s.clear()


for m in range(M):
    a = sys.stdin.readline().strip()
    if ' ' in a:
        calc, num = a.split()
        num = int(num)
    else:
        calc = a

    if calc == 'all':
        all()
    elif calc == 'empty':
        empty()
    elif calc == 'add':
        add(num)
    elif calc == 'remove':
        remove(num)
    elif calc == 'check':
        check(num)
    elif calc == 'toggle':
        toggle(num)
    
