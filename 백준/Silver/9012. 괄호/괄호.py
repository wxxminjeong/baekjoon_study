import sys
input = sys.stdin.readline

T = int(input())

for _ in range(T):
    mystring = str(input())
    mystack = []

    for t in mystring:
        if mystack and mystack[-1] == '(' and t == ')':
            mystack.pop()
        else:
            mystack.append(t)

    if mystack == ['\n']:
        print('YES')
    else:
        print('NO')